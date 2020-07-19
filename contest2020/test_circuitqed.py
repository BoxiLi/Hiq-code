from qutip import basis, fidelity

from custermized_qip.device import Circuit_QED
from custermized_qip.circuit import QubitCircuit

# 定义一个circuit
circuit = QubitCircuit(2)
circuit.add_gate("X", targets=0)
circuit.add_gate("Z", targets=0)
circuit.add_gate("ISWAP", targets=[0,1])

# 定义一个processor
processor = Circuit_QED(2)
# 加载circuit
processor.load_circuit(circuit)
# 计算得到final state （初始值为零态）
final_state = processor.run_state(basis([10, 2, 2])).states[-1]
# print保真度
print(fidelity(final_state.ptrace(1), basis(2,1)))
# 画pulse图
fig, ax = processor.plot_pulses()
fig.savefig("testfig.png")
input()
