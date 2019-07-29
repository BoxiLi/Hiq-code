from projectq.ops import R, X, H, All, Measure
from projectq.meta import Control, Compute, Uncompute
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from projectq.backends import CommandPrinter
from projectq.setups.default import get_engine_list

import numpy as np
import random
import copy
from mpi4py import MPI

#eng = HiQMainEngine(engine_list=get_engine_list()+[CommandPrinter()])
eng = HiQMainEngine(engine_list=get_engine_list())

# number of digits to two sets of qureg
dig_of_qureg = 3

# two qureg of same digits,|unit,tens,hendreds,...>
qureg1 = eng.allocate_qureg(dig_of_qureg)
qureg2 = eng.allocate_qureg(dig_of_qureg)

# quantum fourier transform for qureg
def quantum_fourier(qureg):
    for i in range(len(qureg)):
        H | qureg[-1 - i]
        for j in range(len(qureg) - 1 - i):
            with Control(eng, qureg[-1 - (j + i + 1)]):
                R(np.pi / (1 << (1 + j))) | qureg[-1 - i]

# add qureg1 to transformed qureg2
def quantum_addition(qureg1,qureg2):
    for i in range(len(qureg1)):
        for j in range(len(qureg1) - i):
            with Control(eng, qureg1[j]):
                R(2*np.pi / (1 << (1 + i))) | qureg2[i + j]



# initialize quregs, take |110> + |100> for example
# the output should be |001> in this case
X | qureg1[0]
X | qureg1[1]
X | qureg2[0]

# do QFT to qureg2
with Compute(eng):
    quantum_fourier(qureg2)

# do quantum addition
quantum_addition(qureg1,qureg2)

# reverse QFT to qureg2
Uncompute(eng)


eng.flush()

# cheating wavefunction
mapping, wave_func = copy.deepcopy(eng.backend.cheat())

# print the possibility of the result state for cheating
print(eng.backend.get_probability("001", qureg2))

# measure the qubit with a basis spanned by {|0>, |1>}
All(Measure) | qureg2



# Call the main engine to execute
#print(wave_func)

 # Obtain the output. Note that the result is still stored in the qubit object yet clashed into a classical bit
print("Measured: {}".format([int(qubit) for qubit in qureg2]))

