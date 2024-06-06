import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, xi):
    def L(k, xi):
        Lk = 1
        for j in range(len(x)):
            if j != k:
                Lk *= (xi - x[j]) / (x[k] - x[j])
        return Lk

    yi = 0
    for k in range(len(x)):
        yi += y[k] * L(k, xi)
    return yi

def newton_interpolation(x, y, xi):
    def divided_diff(x, y):
        n = len(y)
        coef = np.zeros([n, n])
        coef[:, 0] = y
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
        return coef[0, :]

    coef = divided_diff(x, y)
    yi = coef[0]
    for i in range(1, len(coef)):
        term = coef[i]
        for j in range(i):
            term *= (xi - x[j])
        yi += term
    return yi

def hasil_interpolasi(x, y):
    xi = np.linspace(5, 40, 10)  #memilih 10 poin dari 5 sampai 40
    print(f"{'xi':^10}{'Lagrange yi':^20}{'Newton yi':^20}")
    print("="*50)
    for xi_i in xi:
        yi_lagrange = lagrange_interpolation(x, y, xi_i)
        yi_newton = newton_interpolation(x, y, xi_i)
        print(f"{xi_i:<10.2f}{yi_lagrange:<20.2f}{yi_newton:<20.2f}")

def grafik_hasil(x, y):
    xi = np.linspace(5, 40, 100)
    yi_lagrange = [lagrange_interpolation(x, y, xi_i) for xi_i in xi]
    yi_newton = [newton_interpolation(x, y, xi_i) for xi_i in xi]

    plt.figure(figsize=(12, 6))
    plt.plot(x, y, 'o', label='Data')
    plt.plot(xi, yi_lagrange, label='Interpolasi Lagrange')
    plt.plot(xi, yi_newton, label='Interpolasi Newton', linestyle='--')
    plt.xlabel('Tegangan (kg/mm²)')
    plt.ylabel('Waktu Patah (jam)')
    plt.legend()
    plt.title('Interpolasi Lagrange and Newton')
    plt.show()
    
def manual_input():
    x = []
    y = []
    print("Masukkan nilai x dan y (ketik 'stop' untuk mengakhiri input):")
    while True:
        x_input = input("Masukkan nilai x: ")
        if x_input.lower() == 'stop':
            break
        y_input = input("Masukkan nilai y: ")
        if y_input.lower() == 'stop':
            break
        try:
            x.append(float(x_input))
            y.append(float(y_input))
        except ValueError:
            print("Nilai x dan y harus berupa angka. Silakan coba lagi.")
    
    return x, y

# Main
x, y = manual_input()
if len(x) < 2 or len(y) < 2:
    print("Data yang dimasukkan tidak cukup untuk melakukan interpolasi.")
else:
    hasil_interpolasi(x, y)
    grafik_hasil(x, y)
