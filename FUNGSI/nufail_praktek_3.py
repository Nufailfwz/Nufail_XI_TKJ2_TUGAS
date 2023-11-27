# NAMA : MUHAMADA NUFAIL FAWWAZ  
# KELAS : XI TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung nilai pangkat dari suatu bilangan
#dengan eksponen tertentu.

def pangkatkan(angka, pangkat):
    hasil_pangkat = angka ** pangkat
    return hasil_pangkat

input_angka = float(input("Masukkan angka: "))
input_pangkat = int(input("Masukkan pangkat (bilangan bulat): "))

hasil_pangkat = pangkatkan(input_angka, input_pangkat)
print(f"{input_angka} pangkat {input_pangkat} adalah {hasil_pangkat}.")
