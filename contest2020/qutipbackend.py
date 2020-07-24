from projectq.backends import IBMBackend
from projectq.cengines import BasicEngine
from projectq.meta import get_control_count, LogicalQubitIDTag
from projectq.ops import All, H, X, Z, Y, CNOT, Measure, FlushGate
from projectq.cengines import (MainEngine,
                               AutoReplacer,
                               LocalOptimizer,
                               TagRemover,
                               DecompositionRuleSet)
from projectq.ops import (NOT,
                          Y,
                          Z,
                          X,
                          T,
                          Tdag,
                          S,
                          Sdag,
                          H,
                          Rx,
                          Ry,
                          Rz,
                          Measure,
                          Allocate,
                          Deallocate,
                          Barrier,
                          FlushGate)
from custermized_qip.device import LinearSpinChain
from custermized_qip.qasm import read_qasm
from qutip import basis, Options
# import projectq.setups

class QutipBackend(BasicEngine):
    def __init__(self, processor, options=None):
        """
        Args:
            processor (qutip.qip.device.Processor): The simulation model in qutip. E.g. LinearSpinchain, CavityQED
        """
        BasicEngine.__init__(self)
        self.processor = processor
        self._reset()
        self.qasm = ""
        self._allocated_qubits = set()
        if options is None:
            self.options = Options()
        else:
            self.options = options
        self.final_state = None

    def is_available(self, cmd):
        """
        Return true if the command can be executed.

        The IBM quantum chip can do X, Y, Z, T, Tdag, S, Sdag,
        rotation gates, barriers, and CX / CNOT.

        Args:
            cmd (Command): Command for which to check availability
        """
        g = cmd.gate
        if g == NOT and get_control_count(cmd) <= 1:
            return True
        if get_control_count(cmd) == 0:
            if g in (H, X, Y, Z):
                return True
            if isinstance(g, (Rx, Ry, Rz)):
                return True
        if g in (Measure, Allocate, Deallocate, Barrier):
            return True
        return False

    def _reset(self):
        """ Reset all temporary variables (after flush gate). """
        self._clear = True

    def _store(self, cmd):
        """
        Copied from IBMBackend._store.
        It transfer the ProjectQ circuit to QASM.
        """
        _gate_names = {str(Tdag): "tdg",
                    str(Sdag): "sdg"}

        if self._clear:
            self._clear = False
            self.qasm = ""
            # self._allocated_qubits = set()

        gate = cmd.gate

        if gate == Allocate:
            self._allocated_qubits.add(cmd.qubits[0][0].id)
            return

        if gate == Deallocate:
            return

        if gate == Measure:
            assert len(cmd.qubits) == 1 and len(cmd.qubits[0]) == 1
            qb_id = cmd.qubits[0][0].id
            logical_id = None
            for t in cmd.tags:
                if isinstance(t, LogicalQubitIDTag):
                    logical_id = t.logical_qubit_id
                    break
            assert logical_id is not None
            # self._measured_ids += [logical_id]
        elif gate == NOT and get_control_count(cmd) == 1:
            ctrl_pos = cmd.control_qubits[0].id
            qb_pos = cmd.qubits[0][0].id
            self.qasm += "\ncx q[{}], q[{}];".format(ctrl_pos, qb_pos)
        elif gate == Barrier:
            qb_pos = [qb.id for qr in cmd.qubits for qb in qr]
            self.qasm += "\nbarrier "
            qb_str = ""
            for pos in qb_pos:
                qb_str += "q[{}], ".format(pos)
            self.qasm += qb_str[:-2] + ";"
        elif isinstance(gate, (Rx, Ry, Rz)):
            assert get_control_count(cmd) == 0
            qb_pos = cmd.qubits[0][0].id
            u_strs = {'Rx': 'u3({}, -pi/2, pi/2)', 'Ry': 'u3({}, 0, 0)',
                      'Rz': 'u1({})'}
            gate = u_strs[str(gate)[0:2]].format(gate.angle)
            self.qasm += "\n{} q[{}];".format(gate, qb_pos)
        else:
            assert get_control_count(cmd) == 0
            if str(gate) in _gate_names:
                gate_str = _gate_names[str(gate)]
            else:
                gate_str = str(gate).lower()

            qb_pos = cmd.qubits[0][0].id
            self.qasm += "\n{} q[{}];".format(gate_str, qb_pos)

    def _run(self):
        """
        Run the circuit.

        Send the circuit via the IBM API (JSON QASM) using the provided user
        data / ask for username & password.
        """
        # return if no operations / measurements have been performed.
        if self.qasm == "":
            return

        max_qubit_id = max(self._allocated_qubits)
        self.qasm = ("OPENQASM 2.0;\ninclude \"qelib1.inc\";\nqreg q[{nq}];\ncreg c[{nq}];"
            + self.qasm).format(nq=max_qubit_id + 1)
        
        qutip_circuit = read_qasm(self.qasm, strmode=True)
        
        self.processor.load_circuit(qutip_circuit, parallel=False)

        if self.final_state is None:
            dims = self.processor.dims
            self.final_state = basis(dims)
        
        self.final_state = self.processor.run_state(self.final_state, options=self.options).states[-1]

    def receive(self, command_list):
        """
        Receives a command list and, for each command, stores it until
        completion.

        Args:
            command_list: List of commands to execute
        """
        for cmd in command_list:
            if not cmd.gate == FlushGate():
                self._store(cmd)
            else:
                self._run()
                self._reset()

    def get_final_state(self, qubits_only=True):
        dims = self.final_state.dims[0]
        qubits_ind = [i for i in range(len(dims)) if dims[i]==2]
        if not qubits_only or len(dims) == len(qubits_ind):
            return self.final_state
        else:
            return self.final_state.ptrace(qubits_ind)
