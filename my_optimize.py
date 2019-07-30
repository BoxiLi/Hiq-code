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
    Find all the single qubit gate untill the first controlled gate,
    try to simplify the gate list with a pre-defined multipul-gate
    """
    # print("initial")
    # for cmd in self._l[idx]:
    #     print(cmd.gate)
    # print()
    cmd_list = self._l[idx]
    limit = len(cmd_list)
    if lim is not None:
        limit = lim
    
    # loop and find the position of all the single qubit gates
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

    for single_gates_pos in all_single_gates_pos:
        # print(limit)
        # print("first and last", first_single_q_gates, last_single_q_gates)
        gates_list = [cmd_list[i].gate for i in single_gates_pos]
        # print("here")
        # for gate in gates_list:
        #     print(gate)
        # find if gates in gates list can be simplified
        to_merge_pos, target_gates = sublist_finder(gates_list, opt_dict)
        # print(target_gates)
        # print("gate pos",gates_pos)
        # print("first", first_single_q_gates)
        # if first_single_q_gates==5:
        #     print("first 5")
        #     print("to_merge_pos", to_merge_pos)
        #     print(gates_list)
        #     # print([cmd.gate for cmd in cmd_list[first_single_q_gates:]])
        #     print("first and last", first_single_q_gates, last_single_q_gates)
        #     print(first_single_q_gates < limit-1)

        if not to_merge_pos: # list is empty: nothing to merge
            raise NotMergeable

        merge_start = to_merge_pos[0]
        merge_end = to_merge_pos[-1]
        # print("len cmd_list", len(cmd_list))
        to_merge_cmd = [cmd_list[i] for i in to_merge_pos]
        new_cmds = to_merge_cmd[0].self_merge_multi(to_merge_cmd, target_gates)
        self._l[idx] = cmd_list[: merge_start] + new_cmds + cmd_list[merge_end+1: ]
        # print("new cmd")
        # for cmd in cmd_list[merge_end: ]:
        #     print(cmd.gate)
        # print()
        # print("after optimize")
        # for cmd in self._l[idx]:
        #     print(cmd.gate)
        # print()
        limit = limit - len(to_merge_pos) + len(target_gates)
        # print("new_limit", limit)
        first_single_q_gates = control_pos + 1
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

##################################
"""
Define class method outside
"""            
Command.self_merge_multi = self_merge_multi
LocalOptimizer._optimize = my_optimize
LocalOptimizer.multigate_merge = multigate_merge
#################################
"""
Pre-defined gate optimization
"""
opt_dict = {(H, Z, H) : (X,),
            (H, X, H) : (Z,), 
            (H, Y, H): (Ph(np.pi), Y),
            (T, T, T, T): (Z,)}

def sublist_finder(mylist, opt_dict):
    matches = []
    pos_list = []
    for i in range(len(mylist)):
        for pattern in opt_dict:
            num_ele = len(pattern)
            if mylist[i] == pattern[0] and tuple(mylist[i:i+num_ele]) == pattern:
                matches.append(pattern)
                pos = list(range(i, i+num_ele))
                return pos, opt_dict[pattern]
    return [],[]

pos_list, new_gates = sublist_finder([H,Z,Z,H,H,Z,H,X,H,X,H], opt_dict)
#################################

# create a list of restriction engines
restric_engine = restrictedgateset.get_engine_list(one_qubit_gates=(X,Y,Z,H,S,T,Rx,Ry,Rz),
                                                two_qubit_gates=(CZ,CX))

eng = HiQMainEngine(backend, engine_list=[CommandPrinter()] + engines + [CommandPrinter()])

qureg = eng.allocate_qureg(2)

H | qureg[0]
X | qureg[0]
H | qureg[0]
CZ | (qureg[0], qureg[1])
H | qureg[0]
X | qureg[0]
H | qureg[0]
# Z | qureg[0]
# H | qureg[0]
# X | qureg[1]
# Z | qureg[1]

All(Measure) | qureg


