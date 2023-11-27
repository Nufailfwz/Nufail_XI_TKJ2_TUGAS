# NAMA : MUHAMAD NUFAIL FAWWAZ
# KELAS : XI - TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Sebuah bakteri pembelahan setiap 20 menit. Sebuah bakteri ditempatkan
#dalam lingkungan yang cocok dan berkembang biak dengan cepat. Buatlah program yang
#menghitung berapa kali pembelahan bakteri terjadi dalam rentang waktu 2 jam.

interval_pemecahan = 20
waktu_total = 120
jumlah_pemecahan = 0

while waktu_total >= interval_pemecahan:
    waktu_total -= interval_pemecahan
    jumlah_pemecahan += 1

print(f'Terjadi pemecahan bakteri sebanyak {jumlah_pemecahan} kali dalam waktu 2 jam.')
