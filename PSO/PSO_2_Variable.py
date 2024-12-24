import random
import math
import matplotlib.pyplot as plt

# fungsi f(x, y)
def func(x, y):
    return x**2 + y**2 - 5 * math.cos(2 * math.pi * x) - 5 * math.cos(2 * math.pi * y) + 10

# Inisialisasi xi, yi, v0, vi, c1, c2, r1, r2, w, gBest, dan pBest
xi = [random.uniform(-5, 5) for _ in range(10)]
yi = [random.uniform(-5, 5) for _ in range(10)]
v0 = [0.0 for _ in range(10)]
vi_x = v0[:]
vi_y = v0[:]
c1 = 1
c2 = 1/2
r1 = r2 = random.uniform(0, 1)
w = 1
gBest = (xi[0], yi[0])
update_pBest = [(x, y) for x, y in zip(xi, yi)]
pBest = [(x, y) for x, y in zip(xi, yi)]
pBest_values = [func(x,y) for x,y in zip (xi,yi)]

#variable tambahan untuk menyimpan nilai gbest minimum dan dimana iterasinya
min_gBest = gBest
min_gBest_iteration = 0

#fungsi untuk memperbarui nilai kecepatan di setiap partikel
def update_vi(v, x, pBest_x, gBest_x, r1, r2):
    return w * v + c1 * r1 * (pBest_x - x) + c2 * r2 * (gBest_x - x)

#fungsi untuk memperbarui nilai posisi di setiap partikel
def update_pos(pos, v):
    return pos + v

# Persiapan plot grid
fig, axes = plt.subplots(5, 6, figsize=(20, 15))
axes = axes.flatten() 

# Memprint nilai awal dari xi, yi, dan v0 
print("\n=================================================================================")
print("Nilai awal  \t    x \t\t    y \t\t F(x, y) \t   v0 \t\t|")
print("=================================================================================")
for i, (x, y, v_0,) in enumerate(zip(xi, yi, v0,), start=1):
    print(f" {i} \t\t {x:.4f} \t {y:.4f} \t {func(x, y):.4f} \t {v_0:.4f} \t|")
print("=================================================================================")
print(f"\t\t\tNilai gBest Minimum x = {gBest[0]:.4f}")
print(f"\t\t\tNilai gBest Minimum y = {gBest[1]:.4f}")
print(f"\t\t\tNilai Minimum f(x, y) = {func(gBest[0], gBest[1]):.4f}")
print("=================================================================================\n")

# Iterasi PSO
for iteration in range(1, 30 + 1):
    # Perbarui kecepatan dan posisi setiap partikel
    for i in range(10):
        vi_x[i] = update_vi(vi_x[i], xi[i], pBest[i][0], gBest[0], r1, r2)
        vi_y[i] = update_vi(vi_y[i], yi[i], pBest[i][1], gBest[1], r1, r2)
        xi[i] = update_pos(xi[i], vi_x[i])
        yi[i] = update_pos(yi[i], vi_y[i])

    for i in range(10):
        # Perbarui nilai pbest jika ditemukan nilai yang lebih baik
        fitness = func(xi[i],yi[i])
        
        if fitness < pBest_values[i]:
            update_pBest[i] = (xi[i],yi[i])
            pBest_values[i] = fitness
        pBest[i] = (xi[i], yi[i])

    # Perbarui gBest berdasarkan pBest minimum
    current_gBest = min(pBest, key=lambda pos: func(pos[0], pos[1]))
    if func(current_gBest[0], current_gBest[1]) < func(gBest[0], gBest[1]):
        min_gBest = current_gBest
        min_gBest_iteration = iteration
        
    # Perbarui gBest berdasarkan pBest minimum
    gBest = min(pBest, key=lambda pos: func(pos[0], pos[1]))


    # Cetak hasil iterasi saat ini
    print()
    print("\n=================================================================================================================================================")
    print(f"Iterasi {iteration}: \t    x \t\t    y \t\t F(x, y) \t   vx \t\t   vy \t\t pbest x \t pbest y \tpbest value \t|")
    print("=================================================================================================================================================")
    for i, (x, y, vx, vy, px, py, value) in enumerate(zip(xi, yi, vi_x, vi_y, [pb[0] for pb in pBest], [pb[1] for pb in pBest],pBest_values), start=1):
        print(f" {i} \t\t {x:.4f} \t {y:.4f} \t {func(x, y):.4f} \t {vx:.4f} \t {vy:.4f} \t {px:.4f} \t {py:.4f} \t {value:.4f} \t|")
    print("=================================================================================================================================================")
    print(f"Nilai gBest Minimum x = {gBest[0]:.4f}")
    print(f"Nilai gBest Minimum y = {gBest[1]:.4f}")
    print(f"Nilai Minimum f(x, y) = {func(gBest[0], gBest[1]):.4f}")
    print("=================================================================================================================================================")

# Plot per iterasi
    ax = axes[iteration - 1]  # Pilih subplot berdasarkan iterasi
    ax.scatter(xi, yi, c='blue', label='Particles')  # Posisi partikel
    ax.scatter(gBest[0], gBest[1], c='red', s=100, label='Global Best')  # gBest
    ax.set_title(f"Iteration {iteration}")
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.legend()
    
# Cetak hasil gBest minimum dari iterasi yang sudah didapatkan
print("\n=================================================")
print("\t\t KESIMPULAN  \t\t\t|")
print("=================================================")
print(f"Nilai gBest Minimum: x = {min_gBest[0]:.4f}, y = {min_gBest[1]:.4f}")
print(f"Nilai Minimum f(x, y) = {func(min_gBest[0], min_gBest[1]):.4f}")
print(f"Didapatkan di iterasi yang ke {min_gBest_iteration}")
print("=================================================")

# Tata letak subplot agar lebih rapi
plt.tight_layout()
plt.savefig("pso_iterations_grid.png")
plt.show()