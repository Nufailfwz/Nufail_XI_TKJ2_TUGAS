# NAMA : MUHAMADA NUFAIL FAWWAZ  
# KELAS : XI TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung bilangan Fibonacci ke-n.

def hitung_fibonacci(x):
    if x <= 0:
        return "Bilangan Fibonacci hanya terdefinisi untuk x >= 1"
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return hitung_fibonacci(x - 1) + hitung_fibonacci(x - 2)

input_nilai = int(input("Masukkan nilai x: "))

if input_nilai <= 0:
    print("Bilangan Fibonacci hanya terdefinisi untuk x >= 1")
else:
    hasil = hitung_fibonacci(input_nilai)
    print(f"Bilangan Fibonacci ke-{input_nilai} adalah {hasil}.")
