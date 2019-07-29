"""
An example of decomposing controlled rotation gate into CX, CZ and single rotation
"""
import copy
import projectq
import numpy as np
from projectq.backends import CommandPrinter
from projectq.ops import BasicGate, Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, QFT
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

backend = SimulatorMPI(gate_fusion=True, num_local_qubits=2)

cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
temp = LocalOptimizer(cache_depth)
engines = [TagRemover()
            , temp
            , AutoReplacer(rule_set)
            , TagRemover()
            , LocalOptimizer(cache_depth)
            , GreedyScheduler()
            ]

# create a list of restriction engines
restric_engine = restrictedgateset.get_engine_list(one_qubit_gates=(X,Y,Z,H,S,T,Rx,Ry,Rz),
                                                two_qubit_gates=(CZ,CX))

eng = HiQMainEngine(backend, engine_list=engines + [CommandPrinter()])

class SqrtYGate(BasicGate):
    """ Square-root X gate class """
    @property
    def matrix(self):
        return (0.5 + 0.5j) * np.matrix([[1, -1], [1, 1]])

    def tex_str(self):
        return r'$\sqrt{Y}$'

    def __str__(self):
        return "SqrtY"

    def get_merged(self, other):
        if isinstance(other, SqrtYGate):
            return Y
        else:
            return super(SqrtYGate, self).get_merged(other)

#: Shortcut (instance of) :class:`projectq.ops.SqrtXGate`
SqrtY = SqrtYGate()

qureg = eng.allocate_qureg(2)

SqrtY | qureg[0]
SqrtY | qureg[0]

All(Measure) | qureg

print(int(qureg[0]))