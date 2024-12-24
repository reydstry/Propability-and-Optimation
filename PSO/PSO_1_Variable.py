import random
import math
import matplotlib.pyplot as plt
from prettytable import PrettyTable

# Fungsi f(x)
def func(x):
    return x ** 2 - 5 * math.cos(2 * math.pi * x) + 10

# Inisialisasi xi, v0, vi, c1, c2, r1, r2, w, gBest, dan pBest
xi = [random.uniform(-5.2, 5.2) for _ in range(10)]
v0 = [0.0 for _ in range(10)]
vi = v0[:]
c1 = 1 / 2
c2 = 1
r1 = r2 = random.uniform(0, 1)
w = 1
gBest = min(xi, key=func)
pBest = xi[:]

# Tambahan variable pembantu
min_gBest = gBest
min_gBest_iteration = 0  

# Output nilai awal
print("Inisialisasi Nilai Awal:")
init_table = PrettyTable()
init_table.field_names = ["Partikel", "Posisi", "F(x)"]
for i, x in enumerate(xi, start=1):
    init_table.add_row([f"x{i}", f"{x:.4f}", f"{func(x):.4f}"])
print(init_table)

# Iterasi PSO
for iteration in range(1, 30 + 1):
    # memperbarui kecepatan dan posisi setiap partikel
    for i in range(10):
        r1, r2 = random.uniform(0, 1), random.uniform(0, 1)
        vi[i] = w * vi[i] + c1 * r1 * (pBest[i] - xi[i]) + c2 * r2 * (gBest - xi[i])
        xi[i] = max(-5.2, min(5.2, xi[i] + vi[i]))  # Pastikan posisi tetap dalam rentang batas

    for i in range(10):
        # perbarui nilai pBest paling minimum
        fitness = func(xi[i])
        if fitness < func(pBest[i]):
            pBest[i] = xi[i]

    # memperbarui gBest berdasarkan nilai pBest minimum
    current_gBest = min(pBest, key=func)
    if func(current_gBest) < func(gBest):
        gBest = current_gBest
        if func(gBest) < func(min_gBest):
            min_gBest = gBest
            min_gBest_iteration = iteration

    # tabel untuk menampilkan hasil setiap iterasi
    table = PrettyTable()
    table.field_names = ["Partikel", "Posisi", "F(x)", "v", "pBest"]
    for i, (x, v, p) in enumerate(zip(xi, vi, pBest), start=1):
        table.add_row([f"x{i}", f"{x:.4f}", f"{func(x):.4f}", f"{v:.4f}", f"{p:.4f}"])

    print(f"\nIterasi {iteration} - Tabel Hasil")
    print(table)

    # print nilai gBest di bawah tabel
    print(f"\nNilai gBest pada Iterasi {iteration}: x = {current_gBest:.4f}, Minimum F(x) = {func(current_gBest):.4f}")

    # scatter plot untuk posisi partikel dan gBest untuk iterasi ini
    plt.scatter(xi, [0] * 10, c='blue', label='Particles')  # Plot partikel
    plt.scatter(gBest, 0, c='red', s=100, label='gBest')  # Plot gBest
    plt.title(f"Iteration {iteration}: Particle Positions")
    plt.xlabel("Particle Index")
    plt.ylabel("Position")
    plt.xlim(-6, 6)
    plt.ylim(-1, 1)
    plt.legend()
    plt.grid()
    plt.show()  # scatter plot ditampilkan setiap iterasi

# print hasil pBest dan gBest minimum dari seluruh iterasi
print("\n=================================================")
print("\t\t KESIMPULAN  \t\t\t|")
print("=================================================")
print(f"Nilai gBest Minimum: x = {min_gBest:.4f}")
print(f"Nilai f(x) Minimum = {func(min_gBest):.4f}")
print(f"Didapatkan di iterasi yang ke {min_gBest_iteration}")
print("=================================================")
