"""
This is an example using QuTiP as the backend for ProjectQ
"""
from projectq.backends import IBMBackend
from projectq import MainEngine
import projectq.setups.ibm
from projectq.ops import All, H, X, Z, Y, T, CNOT, Measure, FlushGate

from qutipbackend import QutipBackend
from custermized_qip.device import LinearSpinChain

# Choose a QuTiP processor as the backend
engine_list  =  []
num_qubits = 2
eng = MainEngine(QutipBackend(LinearSpinChain(num_qubits)), engine_list=engine_list)

# Define a circuit in ProjectQ
quregs = eng.allocate_qureg(num_qubits)
H | quregs[0]
CNOT | (quregs[0], quregs[1])
All(H) | quregs
All(Z) | quregs
Y | quregs[0]
X | quregs[0]
eng.flush()

# get the simulation result
result = eng.backend.final_state
print(result)