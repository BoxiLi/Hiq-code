import math
from projectq import MainEngine
from projectq.ops import X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Measure, All
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.cengines import (MainEngine,
AutoReplacer,
LocalOptimizer,
TagRemover,
InstructionFilter,
DecompositionRuleSet)
import projectq.setups.decompositions
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from mpi4py import MPI
from circuit import run_circuit


################################################
import numpy as np
from scipy.optimize import minimize
############################################


# Function that need to be implemented by the contestants
def calculate_theta(eng, final_state):
    """
    Calculate the optimal theta value.
    Args:
    eng (MainEngine): Main compiler engine to use.
    final_state (list): list of quantum bit states.
    Returns:
    list of best theta values.
    """

    return [0, 0, 0, 0, 0]



def list_to_str(final_state):
    [str(i) for i in final_state]
    str_state = "".join([str(i) for i in final_state])
    return str_state

# ###########################
# # Test for list_to_str
# final_state = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
# str_state = list_to_str(final_state)
# print(str_state)
# ###########################



if __name__ == "__main__":
    # use projectq simulator
    #eng = MainEngine()
    # use hiq simulator
    # TODO carefull with num_local_qubits
    backend = SimulatorMPI(gate_fusion=True, num_local_qubits=15)
    cache_depth = 10
    rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])
    engines = [TagRemover()
                , LocalOptimizer(cache_depth)
                , AutoReplacer(rule_set)
                , TagRemover()
                , LocalOptimizer(cache_depth)
                , GreedyScheduler()
                ]
    # make the compiler and run the circuit on the simulator backend
    eng = HiQMainEngine(backend, engine_list = engines)
    qureg = eng.allocate_qureg(14)
    # Just an example, you need to design more final state cases for testing..
    final_state = [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    # Function that need to be implemented by the contestants
#     theta = calculate_theta(eng, final_state)
#     run_circuit(qureg, theta)
#     eng.flush()
#     print(eng.backend.get_probability(final_state, qureg))
#     All(Measure) | qureg


def measure_amplitude(theta, eng, qureg,  str_state):
    from projectq.ops import Deallocate
    run_circuit(qureg, theta)
    eng.flush()
    amp = eng.backend.get_probability(str_state, qureg)
    All(Measure) | qureg

    # reinitialize to |00000..00>
    for qb in qureg:
        if int(qb):
            X | qb
    eng.flush()

    print(1-amp)
    del qureg
    if amp > 0.5:
        amp = 1
    return 1-amp


theta = np.random.rand(5)*4*np.pi
# measure_amplitude(eng, qureg, theta, list_to_str(final_state))

for temp in range(100):
    amp_error = minimize(measure_amplitude, x0 = theta, args=(eng, qureg, list_to_str(final_state)),
                bounds = [(0, 4*np.pi),
                        (0, 4*np.pi),
                        (0, 4*np.pi),
                        (0, 4*np.pi),
                        (0, 4*np.pi)],
                method = 'L-BFGS-B'
                )
    print(amp_error)
    if amp_error.fun < 0.982:
        break
