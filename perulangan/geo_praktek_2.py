# Nama = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No Absen = 12
# Soal = Deskripsi Pekerjaan: Seorang pelari ingin meningkatkan jarak tempuhnya setiap minggunya. Ia mulai
#        dengan 5 kilometer dan meningkatkan jaraknya sebesar 10% setiap minggunya. Buatlah program
#        yang menghitung berapa minggu yang dibutuhkan agar pelari itu dapat berlari lebih dari 10 kilometer.

jarak_awal = 5
jarak_target = 10
minggu = 0

while jarak_awal <= jarak_target:
    minggu += 1
    tambahan_jarak = jarak_awal * 0.1  # 10% dari jarak pada minggu sebelumnya
    jarak_awal += tambahan_jarak

print(f"Jumlah minggu yang dibutuhkan agar pelari dapat berlari lebih dari 10 km adalah: {minggu}")