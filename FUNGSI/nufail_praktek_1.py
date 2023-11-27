# NAMA : MUHAMADA NUFAIL FAWWAZ  
# KELAS : XI TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Buatlah sebuah fungsi yang menghitung total dari deret bilangan ganjil hingga
#batas tertentu yang ditentukan pengguna.

def hitung_total_deret_ganjil(batas):
    jumlah = 0
    for bilangan in range(1, batas + 1, 2):
        jumlah += bilangan
    return jumlah

batas_input = int(input("Masukkan batas: "))
hasil_perhitungan = hitung_total_deret_ganjil(batas_input)
print(f"Total deret bilangan ganjil hingga batas {batas_input} adalah {hasil_perhitungan}.")
