# nama: Geofani
# kelas: XI TKJ 2
# nomor absen: 12
# soal: Buat program Python yang mengambil data penjualan bulanan produk dan menentukan kategori produk berdasarkan penjualan: • Jika penjualan lebih dari 1000 unit, kategorikan sebagai "Produk Terlaris." • Jika penjualan antara 500 hingga 1000 unit, kategorikan sebagai "Produk Populer." • Jika penjualan kurang dari 500 unit, kategorikan sebagai "Produk Biasa."
penjualan = int(input("Masukkan jumlah penjualan bulanan produk: "))

if penjualan > 1000:
    kategori = "Produk Terlaris"
elif penjualan >= 500:
    kategori = "Produk Populer"
else:
    kategori = "Produk Biasa"
print(f"Produk ini termasuk dalam kategori: {kategori}")