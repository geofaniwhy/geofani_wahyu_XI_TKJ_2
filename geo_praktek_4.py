# nama: Geofani
# kelas: XI TKJ 2
# nomor absen: 12
# soal: Deskripsi Pekerjaan: Sebagai seorang kasir di toko, Anda harus menghitung jumlah diskon berdasarkan total belanjaan pelanggan dan jenis anggota (anggota biasa atau anggota premium).
def hitung_diskon(total_belanjaan, status_anggota):
    if status_anggota == "premium":
        if total_belanjaan > 500000:
            diskon = total_belanjaan * 0.15
        else:
            diskon = total_belanjaan * 0.10
    else:
        if total_belanjaan > 300000:
            diskon = total_belanjaan * 0.07
        else:
            diskon = 0

    return diskon
total_belanjaan = float(input("Masukkan total belanjaan: "))
status_anggota = input("Masukkan status anggota (biasa/premium): ").lower()

if status_anggota not in ["biasa", "premium"]:
    print("Status anggota tidak valid.")
else:
    diskon = hitung_diskon(total_belanjaan, status_anggota)
    if diskon > 0:
        print(f"Diskon yang diberikan: Rp {diskon:.2f}")
    else:
        print("Tidak ada diskon yang diberikan.")