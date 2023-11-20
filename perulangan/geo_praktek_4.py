# Nama = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No Absen = 12
# Soal = Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
# jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa apel kurang dari 20 buah.

jumlah_apel = 100
batas_apel = 20
hari = 0

while jumlah_apel > batas_apel:
    hari += 1
    terjual = jumlah_apel * 0.1 
    jumlah_apel -= terjual

print(f"Jumlah hari yang dibutuhkan agar sisa apel kurang dari 20 buah adalah: {hari}")