"""
This is an example using QuTiP as the backend for ProjectQ
"""
from projectq.backends import IBMBackend
from projectq import MainEngine
from projectq.ops import All, H, X, Z, Y, T, CNOT, Measure, FlushGate

from qutipbackend import QutipBackend
from custermized_qip.device import LinearSpinChain

# Choose a QuTiP processor as the backend
num_qubits = 2
processor = LinearSpinChain(num_qubits, t1=500.)
eng = MainEngine(QutipBackend(processor))

# Define a circuit in ProjectQ
quregs = eng.allocate_qureg(num_qubits)
H | quregs[0]
CNOT | (quregs[0], quregs[1])
All(H) | quregs
All(Z) | quregs
Y | quregs[0]
X | quregs[0]
eng.flush()

# Get the simulation result
final_state = eng.backend.final_state
print(final_state)