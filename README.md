# Tugas-Metode-Numerik
Sistem Persamaan Linear
========================
Pada source code terdapat sebuah penyelesaian untuk masalah sistem persamaan linear. Penyelesaian tersebut menggunakan 3 metode, yaitu :
- Metode Matriks Balikan
- Metode Dekomposisi LU Gauss
- Metode Dekomposisi Crout 

Pada file SPL_Metode_Numerik.py terdapat source code yang dapat digunakan, sedangkan testing.py digunakan untuk mengetes saja.\
Format input matriks ketika menjalankan source code adalah :\
Matriks A:\
1 2 3\
1 2 3\
1 2 3\
Beri spasi untuk menginput elemen selanjutnya.

Implementasi Interpolasi
========================
Pada source code terdapat sebuah penyelesaian interpolasi. Penyelesaian tersebut menggunakan 2 metode, yaitu :
- polinom Langrange
- polinom Newton

Aplikasi Regresi untuk Pemecahan Problem
========================================
Diinginkan untuk mencari hubungan faktor yang mempengaruhi nilai ujian siswa (NT):
- Durasi waktu belajar (TB) terhadap nilai ujian (Problem 1)
- Jumlah latihan soal (NL) terhadap nilai ujian (Problem 2)
- Data TB, NL, dan NT diperoleh dari file yang telah diberikan, yaitu kolom Hours Studied,  Sample Question Papers Practiced, dan Performance Index.

Dalam source code, terdapat Implementasi regresi untuk mencari hubungan tersebut dengan metode:
- Model linear (Metode 1)
- Model eksponensial (Metode 3)

Implementasi Integrasi Numerik untuk Menghitung Estimasi nilai Pi
=================================================================
Nilai pi dapat dihitung secara numerik dengan mencari nilai integral dari fungsi f(x) = 4 / (1 + x^2) dari 0 sampai 1.\
Dalam source code terdapat implementasi penghitungan nilai integral fungsi tersebut secara numerik dengan metode Integrasi trapezoid
