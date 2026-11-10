
# Data nilai 8 siswa
nilai_siswa = [78, 65, 90, 82, 55, 70, 88, 95]

# 1. Menghitung rata-rata nilai
rata_rata = len(nilai_siswa)

print("Rata-rata nilai siswa:", rata_rata)

# 2. Membuat dua List kosong
list_lulus = []
list_remedial = []

# Memisahkan nilai menggunakan for dan if-else
for nilai in nilai_siswa:
    if nilai >= 75:
        list_lulus.append(nilai)
    else:
        list_remedial.append(nilai)

# 3. Menampilkan hasil
print("Daftar nilai siswa yang lulus:")
print(list_lulus)
print("Jumlah siswa lulus:", len(list_lulus))

print("Daftar nilai siswa yang remedial:")
print(list_remedial)
print("Jumlah siswa remedial:", len(list_remedial))
