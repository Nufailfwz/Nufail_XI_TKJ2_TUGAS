# NAMA : MUHAMAD NUFAIL FAWWAZ
# KELAS : XI - TKJ 2 
# NO : 21

#Deskripsi Pekerjaan: Sebuah investasi awal sebesar 10.000 dollar tumbuh sebesar 6% setiap
#tahunnya. Buatlah program yang menghitung berapa tahun yang dibutuhkan agar nilai investasi
#melebihi 20.000 dollar.

awal_investasi = 10000  
target_nilai = 20000 
tingkat_pertumbuhan = 0.06  

tahun = 0  

while awal_investasi < target_nilai:
    awal_investasi += awal_investasi * tingkat_pertumbuhan 
    tahun += 1  
print(f'Dalam waktu {tahun} tahun, nilai investasimu akan berkembang dari {awal_investasi} menjadi lebih dari {target_nilai} dollar.')

