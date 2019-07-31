"""
An example of decomposing controlled rotation gate into CX, CZ and single rotation
"""
import copy
from copy import deepcopy
import projectq
import numpy as np
from projectq.backends import CommandPrinter
from projectq.ops import Allocate, Deallocate, Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Ph
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
import scipy.optimize

from mpi4py import MPI

backend = SimulatorMPI(gate_fusion=True, num_local_qubits=20)

cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
engines = [TagRemover()
            , LocalOptimizer(cache_depth)
            , AutoReplacer(rule_set)
            , TagRemover()
            , LocalOptimizer(cache_depth)
            , GreedyScheduler()
            ]

theta1=np.pi/2
theta2=0
theta3=0
theta4=0
theta5=0



# eng = HiQMainEngine(backend, engine_list=[CommandPrinter()] + engines + [CommandPrinter()])
# eng = HiQMainEngine(backend, engine_list= engines)
# Qureg = eng.allocate_qureg(14)


from circuit import example_circuit
# para = np.array([theta1, theta2, theta3, theta4, theta5], dtype = float)
para = (theta1, theta2, theta3, theta4, theta5)
def measure_amplitude(para):
    eng = HiQMainEngine(backend, engine_list= engines)
    Qureg = eng.allocate_qureg(2)
    # mapping, wave_func = copy.deepcopy(eng.backend.cheat())
    # example_circuit(Qureg, para)
    X | Qureg[0]
    # amp = eng.backend.get_probability("00001111111111", Qureg)
    eng.flush()
    amp = eng.backend.get_probability("00", Qureg)
    print(1-amp)
    All(Measure) | Qureg
    All(Deallocate) | Qureg
    eng.flush()
    del Qureg
    if amp > 0.5:
        amp = 1
    return 1-amp



# A = scipy.optimize.minimize(measure_amplitude, para,
# bounds = [(-np.pi, np.pi),
#           (-np.pi, np.pi),
#           (-np.pi, np.pi),
#           (-np.pi, np.pi),
#           (-np.pi, np.pi)]
# )




# step = 1 # step size
# precision = 0.001 #precision
# max_iters = 2 

# for i in range(max_iters):
#     current_amp = measure_amplitude(para[0], para[1], para[2], para[3], para[4])
#     next_amp_list = np.array([], dtype = float)
#     next_amp_list.append(measure_amplitude(para[0] + step, para[1] + step, para[2] + step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] + step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] + step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] + step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] - step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] - step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] - step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] - step, para[3] + step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] + step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] + step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] + step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] + step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] - step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] - step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] - step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] - step, para[3] - step, para[4] + step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] + step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] + step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] + step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] + step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] - step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] - step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] - step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] - step, para[3] + step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] + step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] + step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] + step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] + step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] + step, para[2] - step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] + step, para[2] - step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] + step, para[1] - step, para[2] - step, para[3] - step, para[4] - step),
#                         measure_amplitude(para[0] - step, para[1] - step, para[2] - step, para[3] - step, para[4] - step))
                        
#     for j in range(32):
#         if next_amp_list(j) - current_amp > 0:
#             break



#example_circuit(Qureg, theta1, theta2, theta3, theta4, theta5)
