import numpy as np
from numpy.linalg import inv, svd, qr
from numpy import unravel_index
# np.set_printoptions(precision=4, formatter="complex")

########################
def exp_sig_x(A, delta_t):
    x =  A * delta_t
    return np.array([[np.cos(x),
                           1j * np.sin(x)],
                          [1j * np.sin(x),
                           np.cos(x)]])

# A = exp_sig_x(-B, delta_t)
# print(A)

# a = -1j*delta_t*(-B)/2*np.array([[0,1],[1,0]])
# print(sc.expm(a))

def exp_sig_z(A, delta_t):
    x = A * delta_t
    return np.array([[np.exp(1j * x), 0],
                      [0, np.exp(-1j * x)]])

# print(exp_sig_z(-B, delta_t))

# b = -1j*delta_t*(-B)/2*np.array([[1,0],[0,-1]])
# print(sc.expm(b))

def exp_sig_xx(A, delta_t):
    x = A * delta_t
    return np.array([[np.cos(x), 0, 0, 1j*np.sin(x)],
                      [0, np.cos(x), 1j*np.sin(x), 0],
                      [0, 1j*np.sin(x), np.cos(x), 0],
                      [1j*np.sin(x), 0, 0, np.cos(x)]])

# c0 = exp_sig_xx(-B, delta_t)
# print(c0)
# print('')
# c1 = -1j*delta_t*(-B)*np.kron(np.array([[0,1],[1,0]]),np.array([[0,1],[1,0]]))
# c2 = sc.expm(c1)
# print(c2)
# print(c0-c2)

def exp_sig_zz(A, delta_t):
    x = A * delta_t
    return np.array([[np.exp(1j * x), 0, 0, 0],
                     [0, np.exp(-1j * x), 0, 0],
                     [0, 0, np.exp(-1j * x), 0],
                     [0, 0, 0, np.exp(1j * x)]])

# d0 = sig_zz(-B, delta_t)

# d1 = -1j*delta_t*(-B)*np.kron(np.array([[1,0],[0,-1]]),np.array([[1,0],[0,-1]]))
# d2 = sc.expm(d1)
# print(d0-d2)
##################################

def dec_kron(mat2dec):
    UA = np.ones((2, 2), dtype=np.complex)
    a = 0
    max_ind = None
    for (i,j) in [(0,0), (0,2), (2,0), (2,2)]:
        nor = np.linalg.norm(mat2dec[i:i+2, j:j+2])
        if nor > a:
            a = nor
            max_ind = (i, j)

    max_pos_sub_mat2dec = np.argmax(np.abs(mat2dec[max_ind[0]:max_ind[0]+2, max_ind[1]:max_ind[1]+2]))
    row_ind, col_ind = unravel_index(max_pos_sub_mat2dec, (2,2))
    for (i,j) in [(0,0), (0,1), (1,0), (1,1)]:
        UA[i,j] = mat2dec[2*i+row_ind, 2*j+col_ind]
    UA = UA/np.sqrt((UA.T.conjugate() @ UA)[0,0])

    UB = mat2dec[max_ind[0]:max_ind[0]+2, max_ind[1]:max_ind[1]+2]
    UB = np.array(UB)
    UB = UB/np.sqrt((UB.T.conjugate() @ UB)[0,0])
    return UA, UB


MMAT = (1/np.sqrt(2.)*
    np.array([[ 1,  0,  0, 1j],
            [ 0, 1j,  1,  0],
            [ 0, 1j, -1,  0],
            [ 1,  0,  0,-1j]], dtype=np.complex))

Lamda = np.array([[ 1, 1,-1, 1],
                [ 1, 1, 1,-1],
                [ 1,-1,-1,-1],
                [ 1,-1, 1, 1]], dtype=np.complex)

U = exp_sig_xx(1., 3*np.pi/4)


U2 = MMAT.T.conjugate() @ U @ MMAT
UR = (U2 + U2.T.conjugate()) / 2
UI = (U2 - U2.T.conjugate()) / 2.j
V2, S, Xd = svd(UI)

T = UR @ Xd
V1, tempC = qr(T)
C = np.diagonal(tempC)
V1 = T/C

UA, UB = dec_kron(MMAT @ V1 @ MMAT.T.conjugate())
VA, VB = dec_kron(MMAT @ Xd @ MMAT.T.conjugate())

#############################################
theta = inv(Lamda) @ np.angle(np.diag(V1.T.conjugate() @ U2 @ Xd.T.conjugate()))

X = np.array([[0, 1],
    [1, 0]], dtype=np.complex)

Z = np.array([[ 1,  0],
    [ 0, -1]], dtype=np.complex)

I2 = np.array([[1 , 0],
    [0 , 1]], dtype=np.complex)


Ra1 = UA
Rb1 = UB
Ra2 = 1.j / np.sqrt(2) * (X + Z) @ exp_sig_x(theta[1] + np.pi / 2, -1)
Ra2 = (1j / np.sqrt(2)) * (X + Z) @ exp_sig_x(theta[1] + np.pi / 2 , -1)
Rb2 = exp_sig_z(theta[3] , -1)
Ra3 = -(1j / np.sqrt(2)) * (X + Z)
Rb3 = exp_sig_z(theta[2] , 1)
Ra4 = VA @ (I2-1j*X) / np.sqrt(2)
Rb4 = VB @ inv((I2 - 1j*X) / np.sqrt(2))

cnot = np.array([[1,0,0,0],
                 [0,1,0,0],
                 [0,0,0,1],
                 [0,0,1,0]], dtype=np.complex)
m1=np.kron(Ra1, Rb1)
cnot
m2=np.kron(Ra2, Rb2)
cnot
m3=np.kron(Ra3, Rb3)
cnot
m4=np.kron(Ra4, Rb4)

res = m1 @ cnot @ m2 @ cnot @ m3 @ cnot @m4
print(res.T.conjugate() @ U)


# Y = np.array([[0,-1.j],[1.j,0]])
# sxx = np.kron(X,X)
# syy = np.kron(Y,Y)
# szz = np.kron(Z,Z)
# I22 = np.kron(I2,I2)
# UD = expm(-1.j*(theta[1]* sxx + theta[2] * syy + theta[3]*szz))
# res2 = expm(1.j*theta[0]*I22) @ np.kron(UA, UB) @ UD @ np.kron(VA, VB)
# print(res2.T.conjugate() @ U)