# Nama  = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No    = 12
# Soal  = Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#         batas tertentu yang ditentukan pengguna. Rumus: Total deret bilangan ganjil = 1 + 3 + 5 + ... + (2n-1)

def total_deret_ganjil(batas):
    total = 0
    for n in range(1, batas + 1):
        bilangan_ganjil = 2 * n - 1
        total += bilangan_ganjil
    return total

batas = int(input("Masukkan batas deret bilangan ganjil: "))
hasil = total_deret_ganjil(batas)
print("Total deret bilangan ganjil hingga batas", batas, "adalah:", hasil)