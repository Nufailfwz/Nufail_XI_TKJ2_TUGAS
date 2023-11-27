# NAMA : MUHAMAD NUFAIL FAWWAZ
# KELAS : XI - TKJ 2 
# NO : 21

#Deskripsi pekerjaan : Seorang petani memilii 100 ekor ayam di peternakannnya. setiap  bulan, jumlah 
#bertambah 5% dari jumlah ayam pada bulan sebeluumnya. Buatlah program yang menghitung
#berapa bulan yang dibutuhkan agar jumlah ayam melebihi 200 ekor

bulan = 0
jumlah_ayam = 100

while jumlah_ayam < 200:
    bulan += 1
    pertambahan_ayam = int(jumlah_ayam * 0.05)
    jumlah_ayam += pertambahan_ayam
    print(f"Setelah {bulan} bulan, jumlah ayam menjadi {jumlah_ayam} ekor.")
