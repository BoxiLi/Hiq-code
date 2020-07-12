from projectq.backends import IBMBackend
from projectq import MainEngine
import projectq.setups.ibm
from projectq.ops import All, H, X, Z, CNOT, Measure, FlushGate
from projectq.cengines import (MainEngine,
                               AutoReplacer,
                               LocalOptimizer,
                               TagRemover,
                               DecompositionRuleSet)

from  custermized_qip.qasm import read_qasm
# projectq.setups.ibm.get_engine_list()
cache_depth = 10
rule_set = DecompositionRuleSet(modules=[projectq.setups.decompositions])

eng = MainEngine(IBMBackend(), engine_list=[])
quregs = eng.allocate_qureg(2)
H | quregs[0]
CNOT | (quregs[0], quregs[1])
All(H) | quregs
All(Z) | quregs

def _run(self):
    """
    Run the circuit.

    Send the circuit via the IBM API (JSON QASM) using the provided user
    data / ask for username & password.
    """
    # finally: add measurements (no intermediate measurements are allowed)
    for measured_id in self._measured_ids:
        qb_loc = self.main_engine.mapper.current_mapping[measured_id]
        self.qasm += "\nmeasure q[{}] -> c[{}];".format(qb_loc,
                                                        qb_loc)

    # return if no operations / measurements have been performed.
    if self.qasm == "":
        return

    max_qubit_id = max(self._allocated_qubits)
    qasm = ("include \"qelib1.inc\";\nqreg q[{nq}];\ncreg c[{nq}];" +
            self.qasm).format(nq=max_qubit_id + 1)
    info = {}
    info['qasms'] = [{'qasm': qasm}]
    info['shots'] = self._num_runs
    info['maxCredits'] = 5
    info['backend'] = {'name': self.device}

IBMBackend._run = _run
eng.backend._run()
max_qubit_id = max(eng.backend._allocated_qubits)
qasm = ("OPENQASM 2.0;\ninclude \"qelib1.inc\";\nqreg q[{nq}];\ncreg c[{nq}];" +
        eng.backend.qasm).format(nq=max_qubit_id + 1)
print(qasm)


import tempfile
with tempfile.NamedTemporaryFile('r+') as f:
    with open(f.name, 'r+') as writing_file:
        writing_file.write(qasm)
    circuit = read_qasm(f.name)

from custermized_qip.device import SpinChain
