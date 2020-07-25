"""
This is an example using QuTiP as the backend for ProjectQ
"""
import numpy as np
from projectq.backends import IBMBackend
from projectq import MainEngine
from projectq.ops import All, H, X, Z, Y, T, CNOT, Measure, FlushGate

from qutip import fidelity, basis, Options
options = Options(nsteps=20000, max_step=0.0001) # options for QuTiP solver
from qutipbackend import QutipBackend
from custermized_qip.device import CircuitQED


# Define a circuit in ProjectQ: DJ algorithm
def DJ_algorith(eng):
    quregs = eng.allocate_qureg(num_qubits)
    X | quregs[2]
    All(H) | quregs
    CNOT | (quregs[0], quregs[2])
    CNOT | (quregs[1], quregs[2])
    H | quregs[0]
    H | quregs[1]
    eng.flush()

# Choose a QuTiP processor as the backend
num_qubits = 3
processor = CircuitQED(num_qubits)
backend = QutipBackend(processor, options=options, schedule=True)
eng = MainEngine(backend)


#################################################
print("No additional noise:")

# execute the circuit
DJ_algorith(eng)
# Get the simulation result
final_state = eng.backend.get_final_state()
# The first two qubits should never be 00 (ideally, here not really)
print("Excution time (us):", eng.backend.processor.get_full_tlist()[-1])
print("The probability of measuring 00 state is\n", fidelity(final_state.ptrace([0, 1]), basis([2, 2])))
# 画 pulse:
fig, ax = eng.backend.processor.plot_pulses()
fig.savefig("DJ_algorithm.png")
print()


#######################################################
print("Noisy circuit with scheduling:")
processor = CircuitQED(num_qubits, t2=20.0)
backend = QutipBackend(processor, options=options, schedule=True)
eng = MainEngine(backend)

# execute the circuit
DJ_algorith(eng)
# Get the simulation result
final_state = eng.backend.get_final_state()
# The first two qubits should never be 00 (ideally, here not really)
print("Excution time (us):", eng.backend.processor.get_full_tlist()[-1])
print("The probability of measuring 00 state is\n", fidelity(final_state.ptrace([0, 1]), basis([2, 2])))
print()


#######################################################
print("Noisy circuit without scheduling:")
processor = CircuitQED(num_qubits, t2=20.0)
backend = QutipBackend(processor, options=options, schedule=False)
eng = MainEngine(backend)

# execute the circuit
DJ_algorith(eng)
# Get the simulation result
final_state = eng.backend.get_final_state()
# The first two qubits should never be 00 (ideally, here not really)
print("Excution time (us):", eng.backend.processor.get_full_tlist()[-1])
print("The probability of measuring 00 state is\n", fidelity(final_state.ptrace([0, 1]), basis([2, 2])))
print()


#######################################################
print("Noisy circuit with external random field:")
np.random.seed(1)
processor = CircuitQED(num_qubits, t2=20.0)
backend = QutipBackend(processor, options=options, schedule=True)

# We define a noise class
from custermized_qip.noise import UserNoise
class ExternalField(UserNoise):
    def get_noisy_dynamics(self, pulses, dims):
        """
        Flunctuation of magnetic field simulated by sigmaz with
        gausian distributed random amplitude for each qubits
        """
        # Compute the random amplitude
        dt = 0.05
        std = 200.  # fluntation of field (MHz)
        t_max = 0.
        for pulse in pulses:
            t_max = max(t_max, pulse.tlist[-1])
        num_steps = int(np.floor(t_max / dt)) + 1
        random_field_coeff = np.random.normal(loc=0, scale=0.05, size=num_steps)
        tlist = np.arange(0, t_max, dt)
        # add noisy pulse
        for i in range(num_qubits, 2*num_qubits + 1):
            pulses[i].add_coherent_noise(
                pulse.qobj, pulse.targets, tlist, random_field_coeff)
        return pulses

backend.processor.add_noise(ExternalField())
eng = MainEngine(backend)

# execute the circuit
DJ_algorith(eng)
# Get the simulation result
final_state = eng.backend.get_final_state()
# The first two qubits should never be 00 (ideally, here not really)
print("Excution time (us):", eng.backend.processor.get_full_tlist()[-1])
print("The probability of measuring 00 state is\n", fidelity(final_state.ptrace([0, 1]), basis([2, 2])))