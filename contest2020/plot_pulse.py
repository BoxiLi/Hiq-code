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
import matplotlib.pyplot as plt
plt.rcParams.update(
    {"font.size": 19,
    "text.usetex": False,
    # 'legend.fontsize': 'x-large',
    'axes.labelsize': 'small',
    # 'axes.titlesize':'x-small',
    'xtick.labelsize':'x-small',
    'ytick.labelsize':'x-small',
    })

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

# execute the circuit
DJ_algorith(eng)

# plot
fig, axis = eng.backend.processor.plot_pulses(figsize=(13, 6), show_axis=True)

tlist = eng.backend.processor.get_full_tlist()
for ax in axis:
    ax.axvline(x=tlist[5], color = "grey", alpha=0.7)
    ax.axvline(x=tlist[14], color = "grey", alpha=0.7)
    ax.axvline(x=tlist[21], color = "grey", alpha=0.7)
    ax.axvline(x=tlist[31], color = "grey", alpha=0.7)
axis[-1].set_xlabel("time (us)")
axis[0].text(tlist[10], 3000, "CNOT", horizontalalignment='center')
axis[0].text(tlist[26], 3000, "CNOT", horizontalalignment='center')


fig.savefig("DJ_algorithm_pulse.pdf")
print()