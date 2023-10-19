# nama: Geofani
# kelas: XI TKJ 2
# nomor absen: 12
# soal: Deskripsi Pekerjaan: Sebagai seorang manajer proyek, Anda harus menentukan apakah suatu proyek akan selesai tepat waktu atau terlambat.
from datetime import datetime
estimasi_selesai = datetime(2023, 10, 8)
tanggal_target = datetime(2023, 10, 27)
if estimasi_selesai <= tanggal_target:
    print("Tepat waktu")
else:
    print("Terlambat")