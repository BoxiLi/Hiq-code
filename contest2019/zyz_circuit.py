from projectq.ops import X, Y, Z, T, H, CNOT, SqrtX, All, Measure
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from projectq.backends import CommandPrinter
from projectq.setups.default import get_engine_list

import numpy as np
import random
import copy
from mpi4py import MPI

from zyz_dec import zyz_dec
from two_qubit_dec import Ra1, Ra2, Ra3, Ra4, Rb1, Rb2, Rb3, Rb4

# Create main engine to compile the code to machine instructions(required)
#eng = HiQMainEngine(SimulatorMPI(gate_fusion=True, num_local_qubits=20))
eng = HiQMainEngine(engine_list=get_engine_list()+[CommandPrinter()])

# Qubit number N
num_of_qubit = 2

# Use the method provided by the main engine to create qubit registers
qureg = eng.allocate_qureg(num_of_qubit)

zyz_dec(Ra1,qureg,0)
zyz_dec(Rb1,qureg,1)
CNOT | (qureg[0],qureg[1])
zyz_dec(Ra2,qureg,0)
zyz_dec(Rb2,qureg,1)
CNOT | (qureg[0],qureg[1])
zyz_dec(Ra3,qureg,0)
zyz_dec(Rb3,qureg,1)
CNOT | (qureg[0],qureg[1])
zyz_dec(Ra4,qureg,0)
zyz_dec(Rb4,qureg,1)

eng.flush()