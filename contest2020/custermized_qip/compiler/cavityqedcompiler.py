# This file is part of QuTiP: Quantum Toolbox in Python.
#
#    Copyright (c) 2011 and later, Paul D. Nation and Robert J. Johansson.
#    All rights reserved.
#
#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are
#    met:
#
#    1. Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#    3. Neither the name of the QuTiP: Quantum Toolbox in Python nor the names
#       of its contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
#    PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#    HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
###############################################################################
import numpy as np

from ..circuit import QubitCircuit, Gate
from .gatecompiler import GateCompiler, _PulseInstruction


__all__ = ['CavityQEDCompiler']


class CavityQEDCompiler(GateCompiler):
    """
    Decompose a :class:`qutip.QubitCircuit` into
    the pulse sequence for the processor.

    Parameters
    ----------
    N: int
        The number of qubits in the system.

    params: dict
        A Python dictionary contains the name and the value of the parameters,
        such as laser frequency, detuning etc.

    wq: list of float
        The frequency of the qubits calculated from
        eps and delta for each qubit.

    Delta: list of float
        The detuning with repect to w0 calculated
        from wq and w0 for each qubit.

    global_phase: bool
        Record of the global phase change and will be returned.

    num_ops: int
        Number of Hamiltonians in the processor.

    Attributes
    ----------
    N: int
        The number of the component systems.

    params: dict
        A Python dictionary contains the name and the value of the parameters,
        such as laser frequency, detuning etc.

    num_ops: int
        Number of control Hamiltonians in the processor.

    gate_decomps: dict
        The Python dictionary in the form of {gate_name: decompose_function}.
        It saves the decomposition scheme for each gate.
    """
    def __init__(self, N, params, global_phase, num_ops):
        super(CavityQEDCompiler, self).__init__(
            N=N, params=params, num_ops=num_ops)
        self.gate_decomps = {"ISWAP": self.iswap_dec,
                             "SQRTISWAP": self.sqrtiswap_dec,
                             "RZ": self.rz_dec,
                             "RX": self.rx_dec,
                             "GLOBALPHASE": self.globalphase_dec
                             }
        self._sx_ind = list(range(0, N))
        self._sz_ind = list(range(N, 2*N))
        self._g_ind = list(range(2*N, 3*N))
        self.wq = np.sqrt(self.params["eps"]**2 + self.params["delta"]**2)
        self.Delta = self.wq - self.params["w0"]
        self.global_phase = global_phase

    def decompose(self, gates, parallel=False):
        tlist, coeffs = super(CavityQEDCompiler, self).decompose(gates, parallel)
        return tlist, coeffs, self.global_phase

    def rz_dec(self, gate):
        """
        Compiler for the RZ gate
        """
        targets = gate.targets
        pulse_ind = self._sz_ind[targets[0]]
        g = self.params["sz"][targets[0]]
        coeff = np.array([np.sign(gate.arg_value) * g])
        tlist = np.array([abs(gate.arg_value) / (2 * g)])
        pulse_coeffs = [(pulse_ind, coeff)]
        return [_PulseInstruction(gate, tlist, pulse_coeffs)]

    def rx_dec(self, gate):
        """
        Compiler for the RX gate
        """
        targets = gate.targets
        pulse_ind = self._sx_ind[targets[0]]
        g = self.params["sx"][targets[0]]
        coeff = np.array([np.sign(gate.arg_value) * g])
        tlist = np.array([abs(gate.arg_value) / (2 * g)])
        pulse_coeffs = [(pulse_ind, coeff)]
        return [_PulseInstruction(gate, tlist, pulse_coeffs)]

    def sqrtiswap_dec(self, gate):
        """
        Compiler for the SQRTISWAP gate

        Notes
        -----
        This version of sqrtiswap_dec has very low fidelity, please use
        iswap
        """
        # FIXME This decomposition has poor behaviour
        q1, q2 = gate.targets
        pulse_coeffs = []
        pulse_ind = self._sz_ind[q1]
        coeff = np.array([self.wq[q1] - self.params["w0"]])
        pulse_coeffs += [(pulse_ind, coeff)]
        pulse_ind = self._sz_ind[q2]
        coeff = np.array([self.wq[q2] - self.params["w0"]])
        pulse_coeffs += [(pulse_ind, coeff)]
        pulse_ind = self._g_ind[q1]
        coeff = np.array([self.params["g"][q1]])
        pulse_coeffs += [(pulse_ind, coeff)]
        pulse_ind = self._g_ind[q2]
        coeff = np.array([self.params["g"][q2]])
        pulse_coeffs += [(pulse_ind, coeff)]

        J = self.params["g"][q1] * self.params["g"][q2] * (
            1 / self.Delta[q1] + 1 / self.Delta[q2]) / 2
        tlist = np.array([(4 * np.pi / abs(J)) / 8])
        instruction_list = [_PulseInstruction(gate, tlist, pulse_coeffs)]

        # corrections
        gate1 = Gate("RZ", [q1], None, arg_value=-np.pi/4) 
        compiled_gate1 = self.rz_dec(gate1)
        instruction_list += compiled_gate1
        gate2 = Gate("RZ", [q2], None, arg_value=-np.pi/4)
        compiled_gate2 = self.rz_dec(gate2)
        instruction_list += compiled_gate2
        gate3 = Gate("GLOBALPHASE", None, None, arg_value=-np.pi/4)
        self.globalphase_dec(gate3)
        return instruction_list

    def iswap_dec(self, gate):
        """
        Compiler for the ISWAP gate
        """
        q1, q2 = gate.targets
        pulse_coeffs = []
        pulse_ind = self._sz_ind[q1]
        coeff = np.array([self.wq[q1] - self.params["w0"]])
        pulse_coeffs += [(pulse_ind, coeff)]
        pulse_ind = self._sz_ind[q2]
        coeff = np.array([self.wq[q2] - self.params["w0"]])
        pulse_coeffs += [(pulse_ind, coeff)]
        pulse_ind = self._g_ind[q1]
        coeff = np.array([self.params["g"][q1]])
        pulse_coeffs += [(pulse_ind, coeff)]
        pulse_ind = self._g_ind[q2]
        coeff = np.array([self.params["g"][q2]])
        pulse_coeffs += [(pulse_ind, coeff)]

        J = self.params["g"][q1] * self.params["g"][q2] * (
            1 / self.Delta[q1] + 1 / self.Delta[q2]) / 2
        tlist = np.array([(4 * np.pi / abs(J)) / 4])
        instruction_list = [_PulseInstruction(gate, tlist, pulse_coeffs)]

        # corrections
        gate1 = Gate("RZ", [q1], None, arg_value=-np.pi/2.)
        compiled_gate1 = self.rz_dec(gate1)
        instruction_list += compiled_gate1
        gate2 = Gate("RZ", [q2], None, arg_value=-np.pi/2)
        compiled_gate2 = self.rz_dec(gate2)
        instruction_list += compiled_gate2
        gate3 = Gate("GLOBALPHASE", None, None, arg_value=-np.pi/2)
        self.globalphase_dec(gate3)
        return instruction_list

    def globalphase_dec(self, gate):
        """
        Compiler for the GLOBALPHASE gate
        """
        self.global_phase += gate.arg_value
