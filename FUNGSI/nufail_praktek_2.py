# NAMA : MUHAMADA NUFAIL FAWWAZ  
# KELAS : XI TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung faktorial dari suatu bilangan.

def hitung_faktorial(x):
    if x == 0:
        return 1
    else:
        hasil_faktorial = 1
        for angka in range(1, x + 1):
            hasil_faktorial *= angka
        return hasil_faktorial

input_angka = int(input("Masukkan angka: "))
hasil_faktorial = hitung_faktorial(input_angka)
print(f"Faktorial dari {input_angka} adalah {hasil_faktorial}.")
