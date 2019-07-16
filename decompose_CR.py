"""
An example of decomposing controlled rotation gate into CX, CZ and single rotation
"""
import copy
import projectq
import numpy as np
from projectq.backends import CommandPrinter
from projectq.ops import Measure, All, H,X,Y,Z,H,S,T,CX,CZ, Rx,Ry,Rz
from projectq.meta import Loop, Compute, Uncompute, Control
from projectq.setups.default import get_engine_list
from projectq.setups import restrictedgateset

# create a list of restriction engines
restric_engine = restrictedgateset.get_engine_list(one_qubit_gates=(X,Y,Z,H,S,T,Rx,Ry,Rz),
                                                two_qubit_gates=(CZ,CX))

eng = projectq.MainEngine(engine_list=restric_engine+get_engine_list()+[CommandPrinter()])
qubit1, qubit2 = eng.allocate_qureg(2)

H | qubit1
with Control(eng, qubit1):
    Rx(np.pi/2) | qubit2
eng.flush() # In order to have all the above gates sent to the simulator and executed
mapping, wavefunc = copy.deepcopy(eng.backend.cheat())

Measure | qubit1 # In order to not deallocate a qubit in a superposition state
Measure | qubit2 # In order to not deallocate a qubit in a superposition state

wavefunc,mapping