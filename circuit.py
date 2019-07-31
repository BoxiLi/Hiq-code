from projectq.ops import Allocate, Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Ph
def run_circuit(qureg, theta):
    theta1 = theta[0]
    theta2 = theta[1]
    theta3 = theta[2]
    theta4 = theta[3]
    theta5 = theta[4]
    # Totally 5 parameters
    # Allocate | Qureg[0]
    # Allocate | Qureg[1]
    # Allocate | Qureg[2]
    # Allocate | Qureg[3]
    # Allocate | Qureg[4]
    # Allocate | Qureg[5]
    # Allocate | Qureg[6]
    # Allocate | Qureg[7]
    # Allocate | Qureg[8]
    # Allocate | Qureg[9]
    # Allocate | Qureg[10]
    # Allocate | Qureg[11]
    # Allocate | Qureg[12]
    # Allocate | Qureg[13]
    X | qureg[0]
    X | qureg[1]
    X | qureg[2]
    X | qureg[3]
    X | qureg[4]
    X | qureg[5]
    X | qureg[6]
    X | qureg[7]
    X | qureg[8]
    X | qureg[9]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[6]
    H | qureg[7]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    H | qureg[10]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    Rz(theta[0]) | qureg[10]
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[10]
    Rx(theta[2]) | qureg[0]
    H | qureg[0]
    H | qureg[1]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[9]
    H | qureg[8]
    H | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[13]
    H | qureg[12]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[1]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    H | qureg[1]
    H | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[4]
    H | qureg[1]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[13]
    H | qureg[12]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[1]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[1]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[11]
    H | qureg[10]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[0]
    H | qureg[1]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[2]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[1]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    H | qureg[5]
    H | qureg[1]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[0]
    H | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[0]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    H | qureg[4]
    H | qureg[5]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[5]
    H | qureg[4]
    H | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[3]
    H | qureg[2]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    H | qureg[12]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[2]
    H | qureg[3]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[3]
    H | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[3]
    H | qureg[1]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[4]
    H | qureg[1]
    H | qureg[2]
    H | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    H | qureg[12]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[3]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[3]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[3]
    H | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[2]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[12]
    H | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[11]
    H | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[12]
    H | qureg[4]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[2]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    H | qureg[4]
    H | qureg[2]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[0]
    Rx(theta[0]) | qureg[10]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    Rz(theta[1]) | qureg[10]
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[10]
    H | qureg[0]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    H | qureg[3]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    H | qureg[5]
    H | qureg[3]
    Rx(theta[0]) | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[3]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[13]
    H | qureg[12]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[3]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[2]
    H | qureg[0]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[3]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[0]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[0]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[3]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[1]
    H | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[0]
    H | qureg[1]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[11]
    H | qureg[10]
    H | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    Rx(theta[2]) | qureg[13]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[6]
    H | qureg[7]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[11]
    H | qureg[10]
    H | qureg[7]
    Rx(theta[2]) | qureg[6]
    Rx(theta[0]) | qureg[4]
    H | qureg[12]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[12]
    Rx(theta[2]) | qureg[4]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    H | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    H | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[0]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[10]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    Rz(theta[3]) | qureg[10]
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[10]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[2]
    H | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[3]
    H | qureg[11]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[3]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[11]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[2]
    Rx(theta[0]) | qureg[10]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    Rz(theta[2]) | qureg[10]
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[10]
    H | qureg[2]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[0]
    H | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    H | qureg[0]
    H | qureg[3]
    H | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[4]
    H | qureg[3]
    H | qureg[0]
    H | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    H | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[2]
    H | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    H | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[0]
    H | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    H | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    H | qureg[4]
    H | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    H | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[5]
    H | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]
    H | qureg[2]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[3]
    H | qureg[2]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[1]
    H | qureg[11]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[11]
    Rx(theta[2]) | qureg[1]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[3]
    H | qureg[4]
    H | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[4]
    H | qureg[5]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[11]
    H | qureg[10]
    H | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[6]
    H | qureg[7]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[7]
    H | qureg[6]
    H | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[7]
    H | qureg[6]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[6]
    Rx(theta[0]) | qureg[7]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[7]
    H | qureg[6]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[1]
    H | qureg[0]
    H | qureg[2]
    H | qureg[3]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[3]
    H | qureg[2]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[0]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[12]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[1], qureg[12] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    H | qureg[0]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[0]
    H | qureg[4]
    H | qureg[5]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[5], qureg[12] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    H | qureg[5]
    H | qureg[4]
    Rx(theta[0]) | qureg[1]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    Rx(theta[2]) | qureg[1]
    H | qureg[3]
    H | qureg[4]
    Rx(theta[0]) | qureg[11]
    H | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[12]
    Rx(theta[2]) | qureg[11]
    H | qureg[4]
    H | qureg[3]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[3]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[0]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[3], qureg[12] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[3]
    Rx(theta[2]) | qureg[2]
    Rx(theta[0]) | qureg[6]
    Rx(theta[0]) | qureg[7]
    Rx(theta[0]) | qureg[12]
    H | qureg[13]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[7], qureg[12] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[13]
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[7]
    Rx(theta[2]) | qureg[6]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[2]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    H | qureg[8]
    H | qureg[9]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    H | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[4]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[4]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[1]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[11]
    H | qureg[1]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[12]
    H | qureg[11]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[1]
    Rx(theta[0]) | qureg[5]
    H | qureg[11]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    H | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[1]
    H | qureg[8]
    H | qureg[9]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    H | qureg[9]
    H | qureg[8]
    Rx(theta[0]) | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    Rx(theta[2]) | qureg[3]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    H | qureg[12]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[9], qureg[12] )
    CX | ( qureg[8], qureg[9] )
    Rx(theta[2]) | qureg[13]
    H | qureg[12]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[1]
    Rx(theta[2]) | qureg[0]
    Rx(theta[0]) | qureg[2]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[5]
    Rx(theta[2]) | qureg[2]
    H | qureg[2]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[2]
    Rx(theta[0]) | qureg[5]
    H | qureg[13]
    CX | ( qureg[5], qureg[6] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[7], qureg[8] )
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[5], qureg[6] )
    H | qureg[13]
    Rx(theta[2]) | qureg[5]
    Rx(theta[0]) | qureg[8]
    Rx(theta[0]) | qureg[9]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[9]
    Rx(theta[2]) | qureg[8]
    H | qureg[0]
    H | qureg[4]
    H | qureg[10]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[3]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    H | qureg[10]
    H | qureg[4]
    H | qureg[0]
    H | qureg[0]
    H | qureg[5]
    H | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[13]
    H | qureg[10]
    H | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[3]
    H | qureg[4]
    H | qureg[11]
    H | qureg[12]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[4]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[4], qureg[11] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[12]
    H | qureg[11]
    H | qureg[4]
    Rx(theta[2]) | qureg[3]
    H | qureg[3]
    Rx(theta[0]) | qureg[4]
    H | qureg[10]
    H | qureg[13]
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    H | qureg[13]
    H | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[3]
    H | qureg[1]
    H | qureg[4]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[4]
    H | qureg[1]
    H | qureg[1]
    H | qureg[5]
    Rx(theta[0]) | qureg[11]
    H | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[3]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    H | qureg[13]
    Rx(theta[2]) | qureg[11]
    H | qureg[5]
    H | qureg[1]
    H | qureg[0]
    Rx(theta[0]) | qureg[5]
    Rx(theta[0]) | qureg[11]
    Rx(theta[0]) | qureg[12]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[1]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[5], qureg[11] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[0], qureg[1] )
    Rx(theta[2]) | qureg[12]
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[5]
    H | qureg[0]
    Rx(theta[0]) | qureg[2]
    H | qureg[4]
    H | qureg[10]
    H | qureg[12]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    Rz(theta[2]) | qureg[12]
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[12]
    H | qureg[10]
    H | qureg[4]
    Rx(theta[2]) | qureg[2]
    H | qureg[2]
    H | qureg[5]
    Rx(theta[0]) | qureg[10]
    H | qureg[13]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[4]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[5], qureg[10] )
    CX | ( qureg[4], qureg[5] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    H | qureg[13]
    Rx(theta[2]) | qureg[10]
    H | qureg[5]
    H | qureg[2]
    Rx(theta[0]) | qureg[8]
    H | qureg[9]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[8], qureg[9] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[0]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[9], qureg[10] )
    CX | ( qureg[8], qureg[9] )
    H | qureg[11]
    H | qureg[10]
    H | qureg[9]
    Rx(theta[2]) | qureg[8]
    Rx(theta[0]) | qureg[2]
    H | qureg[3]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[11]
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[3], qureg[10] )
    CX | ( qureg[2], qureg[3] )
    Rx(theta[2]) | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[3]
    Rx(theta[2]) | qureg[2]
    H | qureg[6]
    H | qureg[7]
    Rx(theta[0]) | qureg[10]
    H | qureg[11]
    CX | ( qureg[6], qureg[7] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[2]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[7], qureg[10] )
    CX | ( qureg[6], qureg[7] )
    H | qureg[11]
    Rx(theta[2]) | qureg[10]
    H | qureg[7]
    H | qureg[6]
    H | qureg[0]
    Rx(theta[0]) | qureg[1]
    H | qureg[10]
    H | qureg[11]
    CX | ( qureg[0], qureg[1] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    Rz(theta[1]) | qureg[11]
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[1], qureg[10] )
    CX | ( qureg[0], qureg[1] )
    H | qureg[11]
    H | qureg[10]
    Rx(theta[2]) | qureg[1]
    H | qureg[0]
    H | qureg[1]
    Rx(theta[0]) | qureg[4]
    Rx(theta[0]) | qureg[10]
    Rx(theta[0]) | qureg[13]
    CX | ( qureg[1], qureg[2] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[12], qureg[13] )
    Rz(theta[1]) | qureg[13]
    CX | ( qureg[12], qureg[13] )
    CX | ( qureg[11], qureg[12] )
    CX | ( qureg[10], qureg[11] )
    CX | ( qureg[4], qureg[10] )
    CX | ( qureg[3], qureg[4] )
    CX | ( qureg[2], qureg[3] )
    CX | ( qureg[1], qureg[2] )
    Rx(theta[2]) | qureg[13]
    Rx(theta[2]) | qureg[10]
    Rx(theta[2]) | qureg[4]
    H | qureg[1]