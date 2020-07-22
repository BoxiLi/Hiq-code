"""
This is an example using QuTiP as the backend for ProjectQ
"""
from qutip import fidelity, basis, Options
from projectq.backends import IBMBackend
from projectq import MainEngine
from projectq.ops import All, H, X, Z, Y, T, CNOT, Measure, FlushGate

from qutipbackend import QutipBackend
from custermized_qip.device import Circuit_QED

# Choose a QuTiP processor as the backend
num_qubits = 3
processor = Circuit_QED(num_qubits)
eng = MainEngine(QutipBackend(processor, options=Options(nsteps=10000)))
# eng = MainEngine()

# Define a circuit in ProjectQ: DJ algorithm
quregs = eng.allocate_qureg(num_qubits)
X | quregs[2]
All(H) | quregs
CNOT | (quregs[0], quregs[2])
CNOT | (quregs[1], quregs[2])
H | quregs[0]
H | quregs[1]
eng.flush()

# Get the simulation result
final_state = eng.backend.get_final_state()
# The first two qubits should never be 00 (ideally, here not really)
print(fidelity(final_state.ptrace([0, 1]), basis([2, 2])))
# 画 pulse:
fig, ax = eng.backend.processor.plot_pulses()
fig.savefig("DJ_algorithm.pdf")

