# NAMA : MUHAMADA NUFAIL FAWWAZ  
# KELAS : XI TKJ 2 
# NO : 21

# Deskripsi Pekerjaan: Buatlah sebuah fungsi untuk menghitung jumlah digit dari suatu bilangan.

def kalkulasi_total_digit(angka):
    jumlah_total = 0
    for digit_karakter in str(angka):
        if digit_karakter.isdigit():
            jumlah_total += int(digit_karakter)
    return jumlah_total

masukkan_angka = input("Masukkan angka: ")

hasil_total_digit = kalkulasi_total_digit(masukkan_angka)
print(f"Total digit dari {masukkan_angka} adalah {hasil_total_digit}.")
