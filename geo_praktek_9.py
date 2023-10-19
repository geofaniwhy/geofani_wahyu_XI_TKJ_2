# nama: Geofani
# kelas: XI TKJ 2
# nomor absen: 12
# soal: Buat program Python yang mengambil durasi peminjaman buku dalam hari dan menentukan jenis pinjaman berdasarkan aturan berikut: • Peminjaman 7 hari atau kurang: "Peminjaman Pendek" • Peminjaman lebih dari 7 hari hingga 30 hari: "Peminjaman Menengah" • Peminjaman lebih dari 30 hari: "Peminjaman Panjang"
durasi_peminjaman = int(input("Masukkan durasi peminjaman buku (dalam hari): "))

if durasi_peminjaman <= 7:
    jenis_peminjaman = "Peminjaman Pendek"
elif durasi_peminjaman <= 30:
    jenis_peminjaman = "Peminjaman Menengah"
else:
    jenis_peminjaman = "Peminjaman Panjang"
print("Jenis peminjaman: " + jenis_peminjaman)