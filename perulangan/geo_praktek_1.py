# Nama = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No Absen = 12
# Soal = Deskripsi Pekerjaan: Seorang petani memiliki 100 ekor ayam di peternakannya. Setiap bulan, jumlah
#        ayam bertambah 5% dari jumlah ayam pada bulan sebelumnya. Buatlah program yang menghitung berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor.

jumlah_ayam = 100
target_ayam = 200
bulan = 0

while jumlah_ayam <= target_ayam:
    bulan += 1
    tambahan_ayam = jumlah_ayam * 0.05  # 5% dari jumlah ayam pada bulan sebelumnya
    jumlah_ayam += tambahan_ayam

print(f"Jumlah bulan yang dibutuhkan agar ayam melebihi 200 ekor adalah: {bulan}")