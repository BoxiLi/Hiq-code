"""
An example of decomposing controlled rotation gate into CX, CZ and single rotation
"""
import copy
import projectq
import numpy as np
from projectq.backends import CommandPrinter
from projectq.ops import BasicGate, Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz
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

backend = SimulatorMPI(gate_fusion=True, num_local_qubits=)

cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
engines = [TagRemover()
            , LocalOptimizer(cache_depth)
            , AutoReplacer(rule_set)
            , TagRemover()
            , LocalOptimizer(cache_depth)
            , GreedyScheduler()
            ]

# create a list of restriction engines
restric_engine = restrictedgateset.get_engine_list(one_qubit_gates=(X,Y,Z,H,S,T,Rx,Ry,Rz),
                                                two_qubit_gates=(CZ,CX))

eng = HiQMainEngine(backend, engine_list=restric_engine + engines + [CommandPrinter()])
qureg = eng.allocate_qureg(2)

H | qureg[0]
with Control(eng, qureg[0]):
    Rx(np.pi/2) | qureg[1]
eng.flush() # In order to have all the above gates sent to the simulator and executed
mapping, wavefunc = copy.deepcopy(eng.backend.cheat())

All(Measure) | qureg

print(wavefunc)
print(mapping)