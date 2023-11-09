# Nama  = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No    = 12
# Soal  = Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
#         dengan eksponen tertentu. Rumus: Bilangan^Eksponen

def hitung_pangkat(bilangan, eksponen):
    hasil = 1
    for _ in range(eksponen):
        hasil *= bilangan
    return hasil
bilangan = float(input("Masukkan bilangan: "))
eksponen = int(input("Masukkan eksponen: "))
hasil_pangkat = hitung_pangkat(bilangan, eksponen)
print(bilangan, "^", eksponen, "adalah:", hasil_pangkat)