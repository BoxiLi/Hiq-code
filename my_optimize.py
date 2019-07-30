"""
An example of decomposing controlled rotation gate into CX, CZ and single rotation
"""
import copy
from copy import deepcopy
import projectq
import numpy as np
from projectq.backends import CommandPrinter
from projectq.ops import Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Ph
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.setups import restrictedgateset
from projectq.cengines import (MainEngine,
                               AutoReplacer,
                               LocalOptimizer,
                               TagRemover,
                               DecompositionRuleSet)
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from hiq.projectq.backends import SimulatorMPI
import projectq.setups.decompositions

from mpi4py import MPI

backend = SimulatorMPI(gate_fusion=True, num_local_qubits=10)

cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
engines = [TagRemover()
            , LocalOptimizer(cache_depth)
            , AutoReplacer(rule_set)
            , TagRemover()
            , LocalOptimizer(cache_depth)
            , GreedyScheduler()
            ]

####################################
# importation for _optimize
from copy import deepcopy as _deepcopy
from projectq.cengines import LastEngineException, BasicEngine
from projectq.ops import FlushGate, FastForwardingGate, NotMergeable, BasicGate, Command
####################################


####################################
"""
Define class method outside
projectq.ops._optimize is overwritten, with a newly added class method
called multigate_merge. It optimizes single-qubit gates with rules
defined in opt_dict
"""
opt_dict = {(H, Z, H) : (X,),
            (H, X, H) : (Z,), 
            (H, Y, H): (Ph(np.pi), Y),
            (T, T, T, T): (Z,)}


def sublist_finder(mylist, opt_dict):
    for i in range(len(mylist)):
        for pattern in opt_dict:
            num_ele = len(pattern)
            if mylist[i] == pattern[0] and tuple(mylist[i:i+num_ele]) == pattern:
                pos = list(range(i, i+num_ele))
                return pos, opt_dict[pattern]
    return [],[]


def my_optimize(self, idx, lim=None):
    """
    Copied from projectq code, only add multigate_merge at the end.

    Try to merge or even cancel successive gates using the get_merged and
    get_inverse functions of the gate (see, e.g., BasicRotationGate).

    It does so for all qubit command lists.
    """
    # loop over all qubit indices
    i = 0
    new_gateloc = 0
    limit = len(self._l[idx])
    if lim is not None:
        limit = lim
        new_gateloc = limit

    while i < limit - 1:
        # can be dropped if two in a row are self-inverses
        inv = self._l[idx][i].get_inverse()

        if inv == self._l[idx][i + 1]:
            # determine index of this gate on all qubits
            qubitids = [qb.id for sublist in self._l[idx][i].all_qubits
                        for qb in sublist]
            gid = self._get_gate_indices(idx, i, qubitids)
            # check that there are no other gates between this and its
            # inverse on any of the other qubits involved
            erase = True
            for j in range(len(qubitids)):
                erase *= (inv == self._l[qubitids[j]][gid[j] + 1])

            # drop these two gates if possible and goto next iteration
            if erase:
                for j in range(len(qubitids)):
                    new_list = (self._l[qubitids[j]][0:gid[j]] +
                                self._l[qubitids[j]][gid[j] + 2:])
                    self._l[qubitids[j]] = new_list
                i = 0
                limit -= 2
                continue

        # gates are not each other's inverses --> check if they're
        # mergeable
        try:
            merged_command = self._l[idx][i].get_merged(
                self._l[idx][i + 1])
            # determine index of this gate on all qubits
            qubitids = [qb.id for sublist in self._l[idx][i].all_qubits
                        for qb in sublist]
            gid = self._get_gate_indices(idx, i, qubitids)

            merge = True
            for j in range(len(qubitids)):
                m = self._l[qubitids[j]][gid[j]].get_merged(
                    self._l[qubitids[j]][gid[j] + 1])
                merge *= (m == merged_command)

            if merge:
                for j in range(len(qubitids)):
                    self._l[qubitids[j]][gid[j]] = merged_command
                    new_list = (self._l[qubitids[j]][0:gid[j] + 1] +
                                self._l[qubitids[j]][gid[j] + 2:])
                    self._l[qubitids[j]] = new_list
                i = 0
                limit -= 1
                continue
        except NotMergeable:
            pass  # can't merge these two commands.

        i += 1  # next iteration: look at next gate
        try:
            limit = self.multigate_merge(idx, lim)
        except NotMergeable:
            pass  # can't merge these two commands.
    return limit


def multigate_merge(self, idx, lim):
    """
    Use the pre-defined single qubit gate optimization in opt_dict
    to simplify the gate list, such as HZH=X.
    """
    # print("initial")
    # for cmd in self._l[idx]:
    #     print(cmd.gate)
    # print()
    cmd_list = self._l[idx]
    limit = len(cmd_list)
    if lim is not None:
        limit = lim
    
    # Divide the cmd list into several sublist containing only
    # single-qubit gates. E.g. [H, X, CZ, X, H] -> [[H, X], [X, H]]
    # all_single_gates_pos store the index of those cmd.
    # E.g all_single_gates_pos = [[0, 1], [3, 4]]
    control_pos = []
    for i in range(limit):
        cmd = cmd_list[i]
        if cmd.control_qubits:
            control_pos.append(i)
    all_single_gates_pos = []
    start = 0
    for p in control_pos:
        all_single_gates_pos.append(list(range(start, p)))
        start = p + 1
    all_single_gates_pos.append(list(range(start, limit)))

    # replace the cmd that can be simplified
    # E.g. [[H, X, H], [X]] -> [[Z], [X]] 
    new_cmd_list = []
    for single_gates_pos in all_single_gates_pos:
        if not single_gates_pos:  # two neighbour controlled gates
            new_cmd_list.append([])
            continue

        # transfer from cmd to gate class
        gates_list = [cmd_list[i].gate for i in single_gates_pos]
        # ind for gates_list and gates class after simplification
        gate_ind, target_gates = sublist_finder(gates_list, opt_dict)
        # ind for cmd_list
        to_merge_pos = [single_gates_pos[ind] for ind in gate_ind]

        if not to_merge_pos: # list is empty: nothing to replace, already optimal
            new_cmd_list.append(cmd_list[single_gates_pos[0]: single_gates_pos[-1]+1])
            continue

        merge_start = to_merge_pos[0]
        merge_end = to_merge_pos[-1]
        to_merge_cmd = [cmd_list[i] for i in to_merge_pos]
        # print("gate to merge")
        # for cmd in to_merge_cmd:
        #     print(cmd.gate)
        # print()
        new_cmd_list.append(
            # not changed
            cmd_list[single_gates_pos[0]: merge_start] +
            # replaced by new cmd
            to_merge_cmd[0].self_merge_multi(to_merge_cmd, target_gates) +
            # not changed
            cmd_list[merge_end+1: single_gates_pos[-1]+1])

    self._l[idx] = []
    for i, p in enumerate(control_pos):
        self._l[idx] += new_cmd_list[i] + [cmd_list[p]]
    self._l[idx] += new_cmd_list[-1]
    limit = len(self._l[idx])
    # print("after optimize")
    # for cmd in self._l[idx]:
    #     print(cmd.gate)
    # print()
    return limit


def self_merge_multi(self, others, target_gates):
    for other in others:
        if (self.tags == other.tags and self.all_qubits == other.all_qubits and
            self.engine == other.engine):
            mergable = True
        else:
            mergable = False
            print("strange things happenedn in merge, check")
    if mergable:
        new_cmds = []
        for i in range(len(target_gates)):
            new_cmds.append(Command(self.engine,
                            target_gates[i],
                            self.qubits,
                            self.control_qubits,
                            deepcopy(self.tags)))
        return new_cmds
    else:
        raise NotMergeable


Command.self_merge_multi = self_merge_multi
LocalOptimizer._optimize = my_optimize
LocalOptimizer.multigate_merge = multigate_merge
#################################


# create a list of restriction engines
restric_engine = restrictedgateset.get_engine_list(one_qubit_gates=(X,Y,Z,H,S,T,Rx,Ry,Rz),
                                                two_qubit_gates=(CZ,CX))

eng = HiQMainEngine(backend, engine_list=[CommandPrinter()] + engines + [CommandPrinter()])

qureg = eng.allocate_qureg(2)

H | qureg[0]
X | qureg[0]
H | qureg[0]
Z | qureg[0]
H | qureg[0]
CZ | (qureg[0], qureg[1])
H | qureg[0]
H | qureg[0]
X | qureg[0]
CZ | (qureg[0], qureg[1])
H | qureg[0]
Z | qureg[0]
H | qureg[0]
H | qureg[0]
X | qureg[1]
Z | qureg[1]

All(Measure) | qureg


