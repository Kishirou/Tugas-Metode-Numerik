import numpy as np

# Solusi Matriks Balikan
def solve_linear_system_inverse(A, b):
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    return x

# Solusi Dekomposisi LU Gauss
def solve_linear_system_LU(A, b):
    n = len(A)
    # Dekomposisi LU
    L, U = lu_decomposition(A)
    # Penyelesaian sistem persamaan linear
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# Dekomposisi LU dengan Metode Eliminasi Gauss
def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.copy(A)

    for i in range(n):
        if U[i][i] == 0:
            raise ValueError("Pembagian oleh nol terdeteksi. Tidak dapat melakukan dekomposisi LU.")
        
        L[i][i] = 1
        for j in range(i+1, n):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor
            for k in range(i, n):
                U[j][k] -= factor * U[i][k]

    return L, U

# Metode substitusi maju
def forward_substitution(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y

# Metode substitusi mundur
def backward_substitution(U, y):
    n = len(U)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if U[i, i] == 0:
            raise ValueError("Pembagian oleh nol terdeteksi. Tidak dapat melakukan substitusi mundur.")
        
        x[i] = (y[i] - np.dot(U[i, i + 1 :], x[i + 1 :])) / U[i, i]
    return x

# Solusi Dekomposisi Crout
def solve_linear_system_Crout(A, b):
    n = len(A)
    # Dekomposisi Crout
    L, U = crout_decomposition(A)
    # Penyelesaian sistem persamaan linear
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x

# Dekomposisi Crout
def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        L[j][j] = 1
        for i in range(j, n):
            U_sum = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - U_sum
        for i in range(j + 1, n):
            L_sum = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = (A[i][j] - L_sum) / U[j][j]

    return L, U

A = np.array([[1, 1, -1], [2, 2, 1], [-1, 1, 1]])
b = np.array([1, 5, 1])

# Solusi Akhir Metode Matriks Balikan
x_inverse = solve_linear_system_inverse(A, b)
print("Metode Matriks Balikan:", x_inverse)

try:
    # Solusi Akhir Metode Dekomposisi LU Gauss
    x_LU = solve_linear_system_LU(A, b)
    print("Metode Dekomposisi LU Gauss:", x_LU)
except ValueError as e:
    print("Error:", e)

# Solusi Akhir Metode Dekomposisi Crout
x_Crout = solve_linear_system_Crout(A, b)
print("Metode Dekomposisi Crout:", x_Crout)
