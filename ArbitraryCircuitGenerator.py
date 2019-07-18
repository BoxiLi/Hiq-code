from projectq.ops import X, Y, Z, T, H, CNOT, SqrtX, All, Measure
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from projectq.backends import CommandPrinter
from projectq.setups.default import get_engine_list

import numpy as np
import random
import copy
from mpi4py import MPI


# Create main engine to compile the code to machine instructions(required)
#eng = HiQMainEngine(SimulatorMPI(gate_fusion=True, num_local_qubits=20))
eng = HiQMainEngine(engine_list=get_engine_list()+[CommandPrinter()])

# Qubit number N
num_of_qubit = 5

#Circuit Depth
depth = 30

# Gate 
gate_set = [X, Y, Z, T, H, SqrtX, CNOT]

# Use the method provided by the main engine to create qubit registers
qureg = eng.allocate_qureg(num_of_qubit)

for i in range(depth):

    
    #Pick random gate from gate_set
    chosen_gate = random.sample(gate_set,1)
    gate = chosen_gate[0]

    #Gate operation
    #If the chosen gate is a two qubit gate
    if gate in [CNOT]:

        #Choose two qubit from qureg
        l = random.sample(qureg,2)

        # To determine the control qubit and target qubit
        m = np.random.randint(0,2)
        if m == 0:
            gate | (l[0],l[1])
        else:
            gate | (l[1],l[0])
    #Is the chosen gate is single qubit gate
    else:
        n = random.sample(qureg,1)
        for qubit in n:
            gate | qubit


    #print("k=",gate,"l=",l)
eng.flush()
mapping, wave_func = copy.deepcopy(eng.backend.cheat())


# Measure the qubit with a basis spanned by {|0>, |1>}
All(Measure) | qureg



# Call the main engine to execute
print(wave_func)

 # Obtain the output. Note that the result is still stored in the qubit object yet clashed into a classical bit
print("Measured: {}".format([int(qubit) for qubit in qureg]))
#print(gate_set)