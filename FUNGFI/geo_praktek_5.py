# Nama  = Geofani Wahyu Nur Pratama
# Kelas = XI TKJ 2
# No    = 12
# Soal  = Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.
#         Rumus: Bilangan Fibonacci ke-n = Bilangan Fibonacci ke-(n-1) + Bilangan Fibonacci ke-(n-2)

def fibonacci(n):
    if n <= 0:
        return "Input harus lebih besar dari 0"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Masukkan nilai n untuk menghitung bilangan Fibonacci ke-n: "))
hasil_fibonacci = fibonacci(n)
print("Bilangan Fibonacci ke-", n, "adalah:", hasil_fibonacci)  