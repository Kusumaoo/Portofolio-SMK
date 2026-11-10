antrean=['Budi','Susi','Anton']

# Menanbahkan pelanggan
antrean.append("Dewi")
print(antrean)

# Menyisipkan pelanggan prioritras
antrean.insert(0, "Pak Kepsek")
print(antrean)

# Menghapus pelanggan
antrean.remove("Susi")
print(antrean)

# Mengganti anton menjadi riko
antrean[2]="Riko"
print(antrean)

# Menampilkan antrean
print("Daftar Antrean Pelanggan:")
for i in antrean(1,6):
  print(i)
