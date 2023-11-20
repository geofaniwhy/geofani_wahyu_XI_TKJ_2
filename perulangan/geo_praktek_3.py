# Nama = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No Absen = 12
# Soal = Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
# tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi melebihi 20.000 dollar.

nilai_awal = 10000
nilai_target = 20000
tahun = 0

while nilai_awal <= nilai_target:
    tahun += 1
    tambahan_nilai = nilai_awal * 0.06 
    nilai_awal += tambahan_nilai

print(f"Jumlah tahun yang dibutuhkan agar nilai investasi melebihi $20,000 adalah: {tahun}")