"""
Simple (Single) Exponential Smoothing
Kasus: Peramalan jumlah pengunjung perpustakaan kampus per minggu

Rumus: S't = alpha * Xt + (1 - alpha) * S't-1
Install: pip install matplotlib
"""

import matplotlib.pyplot as plt
from builtins import abs, enumerate, float, input, len, list, min, print, range, sum, zip

ALPHA_DEFAULT = 0.3


def simple_smoothing(x, alpha):
    """Hitung S't untuk semua periode. S'1 = X1 sebagai nilai awal."""
    s = [x[0]]
    for t in range(1, len(x)):
        s.append(alpha * x[t] + (1 - alpha) * s[t - 1])
    return s


def hitung_error(x, s):
    """MAE dan MSE. Ramalan minggu t adalah S't-1, dibandingkan dengan Xt."""
    selisih = [x[t] - s[t - 1] for t in range(1, len(x))]
    mae = sum(abs(e) for e in selisih) / len(selisih)
    mse = sum(e * e for e in selisih) / len(selisih)
    return mae, mse


def cetak_tabel(x, s):
    """Tampilkan tabel Xt vs S't, baris terakhir adalah ramalan periode berikutnya."""
    print(f"\n{'Minggu ke-':<12}{'Data Aktual (Xt)':<20}{'Nilai Ramalan (S\'t)':<20}")
    print("-" * 52)
    for i, (xi, si) in enumerate(zip(x, s), start=1):
        print(f"{i:<12}{xi:<20}{si:<20.3f}")
    print(f"{len(x) + 1:<12}{'-':<20}{s[-1]:<20.3f}  <- ramalan")


def bandingkan_alpha(x, daftar_alpha=(0.1, 0.3, 0.5, 0.7, 0.9)):
    """Bandingkan beberapa alpha, tandai yang MSE-nya terkecil."""
    hasil = []
    for a in daftar_alpha:
        s = simple_smoothing(x, a)
        mae, mse = hitung_error(x, s)
        hasil.append((a, s[-1], mae, mse))
    terbaik = min(hasil, key=lambda r: r[3])

    print("\nPerbandingan alpha")
    print(f"{'Alpha':<8}{'Ramalan':<12}{'MAE':<12}{'MSE':<12}")
    print("-" * 44)
    for a, fc, mae, mse in hasil:
        tanda = "  <- terbaik" if a == terbaik[0] else ""
        print(f"{a:<8}{fc:<12.2f}{mae:<12.2f}{mse:<12.2f}{tanda}")
    return terbaik[0]


def gambar_grafik(x, s, alpha):
    """Grafik data aktual, hasil smoothing, dan titik ramalan."""
    minggu = list(range(1, len(x) + 1))
    plt.figure(figsize=(9, 5))
    plt.plot(minggu, x, "o-", label="Data aktual (Xt)")
    plt.plot(minggu, s, "s-", label="Smoothing (S't)")
    plt.plot([minggu[-1], minggu[-1] + 1], [s[-1], s[-1]], "g--")
    plt.scatter([minggu[-1] + 1], [s[-1]], color="green", s=80, zorder=5,
                label=f"Ramalan minggu {len(x) + 1}: {s[-1]:.2f}")
    plt.title(f"Simple Exponential Smoothing (alpha = {alpha})")
    plt.xlabel("Minggu ke-")
    plt.ylabel("Jumlah pengunjung")
    plt.xticks(range(1, len(x) + 2))
    plt.grid(alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig("grafik_smoothing.png", dpi=150)
    plt.show()


def main():
    print("=== Peramalan Pengunjung Perpustakaan ===")

    teks = input("Masukkan data aktual per minggu (pisahkan dengan koma): ").strip()

    if not teks:
        print("Data aktual wajib diisi.")
        return

    x = [float(v.strip()) for v in teks.split(",")]

    if len(x) < 2:
        print("Masukkan minimal 2 data minggu.")
        return

    teks = input("Masukkan nilai alpha (0 sampai 1): ").strip()
    alpha = float(teks.replace(",", "."))

    if not 0 < alpha < 1:
        print("Alpha harus lebih besar dari 0 dan lebih kecil dari 1.")
        return

    s = simple_smoothing(x, alpha)
    mae, mse = hitung_error(x, s)

    cetak_tabel(x, s)

    print(f"\nRamalan minggu ke-{len(x) + 1}: {s[-1]:.2f} pengunjung")
    print(f"MAE = {mae:.2f} | MSE = {mse:.2f}")

    gambar_grafik(x, s, alpha)


if __name__ == "__main__":
    main()
