from projectq.ops import Allocate, Measure, All, H, X, Y, Z, H, S, T, CX, CZ, Rx, Ry, Rz, Ph
def example_circuit(Qureg, theta1, theta2, theta3, theta4, theta5):
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
    X | Qureg[0]
    X | Qureg[1]
    X | Qureg[2]
    X | Qureg[3]
    X | Qureg[4]
    X | Qureg[5]
    X | Qureg[6]
    X | Qureg[7]
    X | Qureg[8]
    X | Qureg[9]
    Rx(theta1) | Qureg[0]
    H | Qureg[5]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[5]
    Rx(theta3) | Qureg[0]
    H | Qureg[6]
    H | Qureg[7]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    H | Qureg[7]
    H | Qureg[6]
    Rx(theta1) | Qureg[3]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[0]
    H | Qureg[10]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    Rz(theta1) | Qureg[10]
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[10]
    Rx(theta3) | Qureg[0]
    H | Qureg[0]
    H | Qureg[1]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    H | Qureg[1]
    H | Qureg[0]
    Rx(theta1) | Qureg[8]
    Rx(theta1) | Qureg[9]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[9]
    Rx(theta3) | Qureg[8]
    Rx(theta1) | Qureg[2]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[2]
    H | Qureg[8]
    H | Qureg[9]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[9]
    H | Qureg[8]
    H | Qureg[2]
    H | Qureg[3]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[3]
    H | Qureg[2]
    Rx(theta1) | Qureg[8]
    H | Qureg[9]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[13]
    H | Qureg[12]
    H | Qureg[9]
    Rx(theta3) | Qureg[8]
    H | Qureg[2]
    Rx(theta1) | Qureg[3]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[3]
    H | Qureg[2]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[1]
    H | Qureg[2]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[3]
    H | Qureg[2]
    H | Qureg[1]
    H | Qureg[4]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    H | Qureg[4]
    H | Qureg[1]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[6]
    H | Qureg[7]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[13]
    H | Qureg[12]
    H | Qureg[7]
    Rx(theta3) | Qureg[6]
    H | Qureg[1]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[1]
    Rx(theta1) | Qureg[2]
    H | Qureg[3]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[11]
    H | Qureg[10]
    H | Qureg[3]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[8]
    H | Qureg[9]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[9]
    Rx(theta3) | Qureg[8]
    H | Qureg[0]
    H | Qureg[1]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    H | Qureg[1]
    H | Qureg[0]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[1]
    Rx(theta3) | Qureg[0]
    H | Qureg[2]
    H | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    H | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[2]
    H | Qureg[1]
    H | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    H | Qureg[11]
    H | Qureg[5]
    H | Qureg[1]
    Rx(theta1) | Qureg[1]
    H | Qureg[4]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    H | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[1]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[0]
    H | Qureg[4]
    H | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    H | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[0]
    H | Qureg[8]
    Rx(theta1) | Qureg[9]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[9]
    H | Qureg[8]
    H | Qureg[4]
    H | Qureg[5]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    H | Qureg[5]
    H | Qureg[4]
    H | Qureg[2]
    H | Qureg[3]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[3]
    H | Qureg[2]
    H | Qureg[6]
    Rx(theta1) | Qureg[7]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[7]
    H | Qureg[6]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[3]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[0]
    H | Qureg[1]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    H | Qureg[12]
    H | Qureg[1]
    Rx(theta3) | Qureg[0]
    H | Qureg[2]
    H | Qureg[3]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    H | Qureg[3]
    H | Qureg[2]
    H | Qureg[3]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[3]
    H | Qureg[1]
    H | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    H | Qureg[4]
    H | Qureg[1]
    H | Qureg[2]
    H | Qureg[5]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    H | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[2]
    H | Qureg[5]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    H | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[2]
    H | Qureg[3]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    H | Qureg[12]
    H | Qureg[3]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[5]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[2]
    H | Qureg[4]
    Rx(theta1) | Qureg[5]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[5]
    H | Qureg[4]
    H | Qureg[3]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[4]
    H | Qureg[3]
    H | Qureg[8]
    H | Qureg[9]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[9]
    H | Qureg[8]
    Rx(theta1) | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[1]
    Rx(theta3) | Qureg[0]
    H | Qureg[3]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[3]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[1]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[4]
    H | Qureg[3]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    H | Qureg[3]
    H | Qureg[2]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    H | Qureg[2]
    Rx(theta1) | Qureg[1]
    H | Qureg[4]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[12]
    H | Qureg[11]
    H | Qureg[4]
    Rx(theta3) | Qureg[1]
    H | Qureg[3]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[11]
    H | Qureg[3]
    H | Qureg[4]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[12]
    H | Qureg[4]
    H | Qureg[4]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[5]
    H | Qureg[4]
    Rx(theta1) | Qureg[6]
    Rx(theta1) | Qureg[7]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[7]
    Rx(theta3) | Qureg[6]
    H | Qureg[2]
    H | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    H | Qureg[10]
    H | Qureg[4]
    H | Qureg[2]
    H | Qureg[0]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[1]
    H | Qureg[0]
    Rx(theta1) | Qureg[6]
    H | Qureg[7]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[7]
    Rx(theta3) | Qureg[6]
    Rx(theta1) | Qureg[0]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[0]
    H | Qureg[8]
    Rx(theta1) | Qureg[9]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[9]
    H | Qureg[8]
    Rx(theta1) | Qureg[6]
    H | Qureg[7]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[7]
    Rx(theta3) | Qureg[6]
    H | Qureg[0]
    Rx(theta1) | Qureg[10]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    Rz(theta2) | Qureg[10]
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[10]
    H | Qureg[0]
    H | Qureg[0]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[1]
    H | Qureg[0]
    H | Qureg[3]
    H | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    H | Qureg[11]
    H | Qureg[5]
    H | Qureg[3]
    Rx(theta1) | Qureg[2]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[2]
    H | Qureg[8]
    Rx(theta1) | Qureg[9]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[9]
    H | Qureg[8]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[1]
    H | Qureg[3]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    H | Qureg[3]
    Rx(theta1) | Qureg[6]
    Rx(theta1) | Qureg[7]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[7]
    Rx(theta3) | Qureg[6]
    Rx(theta1) | Qureg[1]
    H | Qureg[4]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[4]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[4]
    H | Qureg[5]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[13]
    H | Qureg[12]
    H | Qureg[5]
    Rx(theta3) | Qureg[4]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[5]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[4]
    H | Qureg[0]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta4) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[0]
    Rx(theta1) | Qureg[4]
    H | Qureg[5]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[5]
    Rx(theta3) | Qureg[4]
    Rx(theta1) | Qureg[3]
    H | Qureg[4]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    H | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[3]
    H | Qureg[2]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[2]
    H | Qureg[0]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta4) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    H | Qureg[0]
    H | Qureg[2]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[2]
    H | Qureg[6]
    Rx(theta1) | Qureg[7]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[7]
    H | Qureg[6]
    Rx(theta1) | Qureg[0]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta4) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[1]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[1]
    H | Qureg[3]
    H | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    H | Qureg[4]
    H | Qureg[3]
    Rx(theta1) | Qureg[6]
    Rx(theta1) | Qureg[7]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[7]
    Rx(theta3) | Qureg[6]
    Rx(theta1) | Qureg[1]
    H | Qureg[5]
    H | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    H | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[3]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[3]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[0]
    H | Qureg[1]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[11]
    H | Qureg[10]
    H | Qureg[1]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[0]
    H | Qureg[5]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    H | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[1]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[1]
    Rx(theta3) | Qureg[0]
    H | Qureg[5]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    Rx(theta3) | Qureg[13]
    H | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[3]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[3]
    H | Qureg[2]
    Rx(theta1) | Qureg[6]
    H | Qureg[7]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[11]
    H | Qureg[10]
    H | Qureg[7]
    Rx(theta3) | Qureg[6]
    Rx(theta1) | Qureg[4]
    H | Qureg[12]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[12]
    Rx(theta3) | Qureg[4]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[4]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[3]
    H | Qureg[5]
    H | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    H | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[0]
    H | Qureg[2]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[2]
    H | Qureg[10]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    Rz(theta4) | Qureg[10]
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[10]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[1]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[3]
    H | Qureg[2]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[8]
    H | Qureg[9]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[9]
    Rx(theta3) | Qureg[8]
    H | Qureg[2]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    H | Qureg[2]
    H | Qureg[8]
    Rx(theta1) | Qureg[9]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[9]
    H | Qureg[8]
    Rx(theta1) | Qureg[3]
    H | Qureg[11]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta4) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[11]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[12]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[2]
    H | Qureg[4]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[5]
    H | Qureg[4]
    Rx(theta1) | Qureg[2]
    H | Qureg[5]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[5]
    Rx(theta3) | Qureg[2]
    H | Qureg[2]
    Rx(theta1) | Qureg[10]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    Rz(theta3) | Qureg[10]
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[10]
    H | Qureg[2]
    Rx(theta1) | Qureg[4]
    H | Qureg[5]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[5]
    Rx(theta3) | Qureg[4]
    H | Qureg[2]
    Rx(theta1) | Qureg[5]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[0]
    H | Qureg[0]
    H | Qureg[5]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[5]
    H | Qureg[0]
    H | Qureg[3]
    H | Qureg[4]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    H | Qureg[4]
    H | Qureg[3]
    H | Qureg[0]
    H | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    H | Qureg[5]
    H | Qureg[0]
    Rx(theta1) | Qureg[2]
    H | Qureg[5]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    H | Qureg[10]
    H | Qureg[5]
    Rx(theta3) | Qureg[2]
    H | Qureg[6]
    Rx(theta1) | Qureg[7]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[7]
    H | Qureg[6]
    Rx(theta1) | Qureg[8]
    Rx(theta1) | Qureg[9]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[9]
    Rx(theta3) | Qureg[8]
    Rx(theta1) | Qureg[0]
    H | Qureg[5]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    H | Qureg[10]
    H | Qureg[5]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[3]
    H | Qureg[4]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[4]
    Rx(theta3) | Qureg[3]
    H | Qureg[4]
    H | Qureg[5]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[5]
    H | Qureg[4]
    H | Qureg[1]
    H | Qureg[4]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[4]
    H | Qureg[1]
    H | Qureg[4]
    Rx(theta1) | Qureg[5]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[5]
    H | Qureg[4]
    H | Qureg[0]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[5]
    H | Qureg[0]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[4]
    H | Qureg[1]
    H | Qureg[2]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[3]
    H | Qureg[2]
    Rx(theta1) | Qureg[2]
    H | Qureg[3]
    Rx(theta1) | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[3]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[1]
    H | Qureg[11]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[11]
    Rx(theta3) | Qureg[1]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[3]
    H | Qureg[4]
    H | Qureg[5]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    H | Qureg[5]
    H | Qureg[4]
    Rx(theta1) | Qureg[4]
    H | Qureg[5]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[11]
    H | Qureg[10]
    H | Qureg[5]
    Rx(theta3) | Qureg[4]
    H | Qureg[0]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[0]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[2]
    H | Qureg[6]
    H | Qureg[7]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    H | Qureg[7]
    H | Qureg[6]
    H | Qureg[6]
    H | Qureg[7]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[7]
    H | Qureg[6]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[5]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[5]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[4]
    H | Qureg[3]
    Rx(theta1) | Qureg[4]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[4]
    H | Qureg[3]
    H | Qureg[6]
    Rx(theta1) | Qureg[7]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[7]
    H | Qureg[6]
    H | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[1]
    H | Qureg[0]
    H | Qureg[2]
    H | Qureg[3]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    H | Qureg[3]
    H | Qureg[2]
    H | Qureg[1]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[1]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[0]
    H | Qureg[0]
    Rx(theta1) | Qureg[1]
    H | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[1], Qureg[12] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[1]
    H | Qureg[0]
    H | Qureg[0]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    H | Qureg[0]
    H | Qureg[4]
    H | Qureg[5]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[5], Qureg[12] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    H | Qureg[5]
    H | Qureg[4]
    Rx(theta1) | Qureg[1]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    Rx(theta3) | Qureg[1]
    H | Qureg[3]
    H | Qureg[4]
    Rx(theta1) | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[12]
    Rx(theta3) | Qureg[11]
    H | Qureg[4]
    H | Qureg[3]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[3]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[3]
    Rx(theta3) | Qureg[2]
    H | Qureg[1]
    Rx(theta1) | Qureg[4]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[4]
    H | Qureg[1]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[3]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta1) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[3], Qureg[12] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[3]
    Rx(theta3) | Qureg[2]
    Rx(theta1) | Qureg[6]
    Rx(theta1) | Qureg[7]
    Rx(theta1) | Qureg[12]
    H | Qureg[13]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[7], Qureg[12] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[13]
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[7]
    Rx(theta3) | Qureg[6]
    H | Qureg[0]
    Rx(theta1) | Qureg[5]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta3) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[5]
    H | Qureg[0]
    H | Qureg[3]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[3]
    H | Qureg[0]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[0]
    H | Qureg[8]
    H | Qureg[9]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    H | Qureg[9]
    H | Qureg[8]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[4]
    H | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta5) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[1]
    H | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[11]
    H | Qureg[1]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[4]
    H | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[12]
    H | Qureg[11]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[3]
    H | Qureg[1]
    Rx(theta1) | Qureg[5]
    H | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    H | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[1]
    H | Qureg[8]
    H | Qureg[9]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    H | Qureg[9]
    H | Qureg[8]
    Rx(theta1) | Qureg[3]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    Rx(theta3) | Qureg[3]
    Rx(theta1) | Qureg[8]
    Rx(theta1) | Qureg[9]
    H | Qureg[12]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[9], Qureg[12] )
    CX | ( Qureg[8], Qureg[9] )
    Rx(theta3) | Qureg[13]
    H | Qureg[12]
    Rx(theta3) | Qureg[9]
    Rx(theta3) | Qureg[8]
    Rx(theta1) | Qureg[0]
    Rx(theta1) | Qureg[1]
    H | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[1]
    Rx(theta3) | Qureg[0]
    Rx(theta1) | Qureg[2]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[5]
    Rx(theta3) | Qureg[2]
    H | Qureg[2]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[2]
    Rx(theta1) | Qureg[5]
    H | Qureg[13]
    CX | ( Qureg[5], Qureg[6] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[7], Qureg[8] )
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[5], Qureg[6] )
    H | Qureg[13]
    Rx(theta3) | Qureg[5]
    Rx(theta1) | Qureg[8]
    Rx(theta1) | Qureg[9]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[9]
    Rx(theta3) | Qureg[8]
    H | Qureg[0]
    H | Qureg[4]
    H | Qureg[10]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta4) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    H | Qureg[10]
    H | Qureg[4]
    H | Qureg[0]
    H | Qureg[0]
    H | Qureg[5]
    H | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[13]
    H | Qureg[10]
    H | Qureg[5]
    H | Qureg[0]
    Rx(theta1) | Qureg[3]
    H | Qureg[4]
    H | Qureg[11]
    H | Qureg[12]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta5) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[4], Qureg[11] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[12]
    H | Qureg[11]
    H | Qureg[4]
    Rx(theta3) | Qureg[3]
    H | Qureg[3]
    Rx(theta1) | Qureg[4]
    H | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    H | Qureg[13]
    H | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[3]
    H | Qureg[1]
    H | Qureg[4]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[4]
    H | Qureg[1]
    H | Qureg[1]
    H | Qureg[5]
    Rx(theta1) | Qureg[11]
    H | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta4) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    H | Qureg[13]
    Rx(theta3) | Qureg[11]
    H | Qureg[5]
    H | Qureg[1]
    H | Qureg[0]
    Rx(theta1) | Qureg[5]
    Rx(theta1) | Qureg[11]
    Rx(theta1) | Qureg[12]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta2) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[5], Qureg[11] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[0], Qureg[1] )
    Rx(theta3) | Qureg[12]
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[5]
    H | Qureg[0]
    Rx(theta1) | Qureg[2]
    H | Qureg[4]
    H | Qureg[10]
    H | Qureg[12]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    Rz(theta3) | Qureg[12]
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[12]
    H | Qureg[10]
    H | Qureg[4]
    Rx(theta3) | Qureg[2]
    H | Qureg[2]
    H | Qureg[5]
    Rx(theta1) | Qureg[10]
    H | Qureg[13]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta5) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[5], Qureg[10] )
    CX | ( Qureg[4], Qureg[5] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    H | Qureg[13]
    Rx(theta3) | Qureg[10]
    H | Qureg[5]
    H | Qureg[2]
    Rx(theta1) | Qureg[8]
    H | Qureg[9]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[8], Qureg[9] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta1) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[9], Qureg[10] )
    CX | ( Qureg[8], Qureg[9] )
    H | Qureg[11]
    H | Qureg[10]
    H | Qureg[9]
    Rx(theta3) | Qureg[8]
    Rx(theta1) | Qureg[2]
    H | Qureg[3]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[11]
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[3], Qureg[10] )
    CX | ( Qureg[2], Qureg[3] )
    Rx(theta3) | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[3]
    Rx(theta3) | Qureg[2]
    H | Qureg[6]
    H | Qureg[7]
    Rx(theta1) | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[6], Qureg[7] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta3) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[7], Qureg[10] )
    CX | ( Qureg[6], Qureg[7] )
    H | Qureg[11]
    Rx(theta3) | Qureg[10]
    H | Qureg[7]
    H | Qureg[6]
    H | Qureg[0]
    Rx(theta1) | Qureg[1]
    H | Qureg[10]
    H | Qureg[11]
    CX | ( Qureg[0], Qureg[1] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    Rz(theta2) | Qureg[11]
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[1], Qureg[10] )
    CX | ( Qureg[0], Qureg[1] )
    H | Qureg[11]
    H | Qureg[10]
    Rx(theta3) | Qureg[1]
    H | Qureg[0]
    H | Qureg[1]
    Rx(theta1) | Qureg[4]
    Rx(theta1) | Qureg[10]
    Rx(theta1) | Qureg[13]
    CX | ( Qureg[1], Qureg[2] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[12], Qureg[13] )
    Rz(theta2) | Qureg[13]
    CX | ( Qureg[12], Qureg[13] )
    CX | ( Qureg[11], Qureg[12] )
    CX | ( Qureg[10], Qureg[11] )
    CX | ( Qureg[4], Qureg[10] )
    CX | ( Qureg[3], Qureg[4] )
    CX | ( Qureg[2], Qureg[3] )
    CX | ( Qureg[1], Qureg[2] )
    Rx(theta3) | Qureg[13]
    Rx(theta3) | Qureg[10]
    Rx(theta3) | Qureg[4]
    H | Qureg[1]