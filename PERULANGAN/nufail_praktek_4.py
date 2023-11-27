# NAMA : MUHAMAD NUFAIL FAWWAZ
# KELAS : XI - TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Seorang pedagang memiliki 100 buah apel. Setiap harinya, ia menjual 10% dari
#jumlah apel yang tersisa. Buatlah program yang menghitung berapa hari yang dibutuhkan agar sisa
#apel kurang dari 20 buah.

awal_apel = 100
batas_jumlah = 20
persen_terjual = 0.10
waktu = 0

while awal_apel > batas_jumlah:
    terjual = awal_apel * persen_terjual
    awal_apel -= terjual
    waktu += 1

print(f'Dibutuhkan {waktu} hari agar sisa buah apel kurang dari {batas_jumlah}.')
