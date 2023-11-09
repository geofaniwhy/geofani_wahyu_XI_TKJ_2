# Nama  = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No    = 12
# Soal  = Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.
#         Rumus: Jumlah digit dari bilangan n = jumlah dari setiap digit dalam n

def hitung_jumlah_digit(bilangan):
    bilangan_str = str(bilangan)
    jumlah_digit = 0
    for digit in bilangan_str:
        if digit.isdigit():
            jumlah_digit += int(digit)
    return jumlah_digit

bilangan = int(input("Masukkan bilangan: "))
hasil_jumlah_digit = hitung_jumlah_digit(bilangan)
print("Jumlah digit dari", bilangan, "adalah:", hasil_jumlah_digit)