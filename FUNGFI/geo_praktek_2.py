# Nama  = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No    = 12
# Soal  = Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.
#         Rumus: Faktorial n = n * (n-1) * (n-2) * ... * 1

def hitung_faktorial(n):
    if n < 0:
        return "Faktorial tidak terdefinisi untuk bilangan negatif"
    elif n == 0:
        return 1
    else:
        faktorial = 1
        for i in range(1, n + 1):
            faktorial *= i
        return faktorial

bilangan = int(input("Masukkan bilangan untuk menghitung faktorial: "))
hasil_faktorial = hitung_faktorial(bilangan)
print("Faktorial dari", bilangan, "adalah:", hasil_faktorial)