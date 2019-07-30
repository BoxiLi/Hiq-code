from projectq.ops import X, Y, Z, T, H, CNOT, SqrtX, All, Measure, Rx, Ph, BasicGate
from hiq.projectq.backends import SimulatorMPI
from hiq.projectq.cengines import GreedyScheduler, HiQMainEngine
from projectq.backends import CommandPrinter
from projectq.setups.default import get_engine_list

import numpy as np
import random
import copy
from mpi4py import MPI

eng = HiQMainEngine(engine_list=get_engine_list()+[CommandPrinter()])

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




opt_dict = {(H, Z, H) : (X),
            (H, X, H) : (Z), 
            (H, Y, H): (Ph(np.pi), Y),
            (T, T, T, T): (Z)}

num_of_qubit = 2

qureg = eng.allocate_qureg(num_of_qubit)

X | qureg[0]

eng.flush()
#mapping, wave_func = copy.deepcopy(eng.backend.cheat())


# Measure the qubit with a basis spanned by {|0>, |1>}
All(Measure) | qureg



# Call the main engine to execute
#print(wave_func)

 # Obtain the output. Note that the result is still stored in the qubit object yet clashed into a classical bit
print("Measured: {}".format([int(qubit) for qubit in qureg]))
#print(gate_set)