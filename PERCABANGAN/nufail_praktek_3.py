# NAMA : MUHAMADA NUFAIL FAWWAZ  
# KELAS : XI TKJ 2 
# NO : 21

# Soal 3:
# Deskripsi Pekerjaan: Sebagai seorang sistem administrator, Anda bertanggung jawab untuk
# memeriksa apakah suatu file di server sudah ada atau belum sebelum menggantinya.
#Soal:
# Buat program Python yang memeriksa apakah suatu file sudah ada di direktori server. Jika file sudah
#ada, program harus mencetak "File sudah ada," jika tidak, program harus mencetak "File belum
#ada."

nama_file = "data.txt"
daftar_file_di_server = ["file1.txt", "file2.txt", "file3.txt"]


if nama_file in daftar_file_di_server:
    print("file ada")
else:
    print("file tidak ada")