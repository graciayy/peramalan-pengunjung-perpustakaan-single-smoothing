# Peramalan Pengunjung Perpustakaan dengan Single Smoothing

Tugas Kelompok 2 - Kelas 5 TI 6, Prodi Teknik Informatika,
Politeknik Negeri Manado (2026).
Dosen pengampu: Christopel H. Simanjuntak, ST, M.Eng

## Deskripsi
Program Python untuk meramalkan jumlah pengunjung perpustakaan kampus
pada minggu berikutnya dengan metode Single (Simple) Exponential Smoothing.

Rumus: S't = α · Xt + (1 − α) · S't-1, dengan S'1 = X1.

## Contoh kasus
- Data 5 minggu: 210, 225, 218, 240, 232
- α = 0,3
- Ramalan minggu ke-6: 225,62 pengunjung
- MAE = 13,02 | MSE = 229,53

## Fitur
- Input data dan nilai α secara interaktif (dengan validasi)
- Tabel data aktual vs nilai smoothing
- Perhitungan MAE dan MSE
- Grafik data aktual, smoothing, dan ramalan (grafik_smoothing.png)

## Cara menjalankan
pip install matplotlib
python simple_smoothing.py

## Anggota Kelompok 2
[Gracia Ester Tendean] [24024146]
[Julio Rifaldo Patroli] [24024151]
[Ferginia Frili Sengka] [24024168]


