""" Tugas File Python
Algoritma dan Pemrograman AC 19 Mei 2022 """

kum_nama = []
kum_umur = []
for i in range(5):
    #Menginputkan nama orang
    nama_orang = input("Masukkan Nama Orang : ")
    kum_nama.append(nama_orang)
print("\n")

i=5
j=0

while i>j:
    #try and except
    try:
        #Menginputkan umur orang
        umur_orang = int(input("Masukkan Umur Orang : "))
        j+=1
    except ValueError:
        j=0
        print("Inputan Salah!") #Peringatan!
        kum_umur = []
        continue

    #fungsi else dan finally
    else:
        kum_umur.append(umur_orang)
    finally:
        pass
file_Nama = open("Nama.txt", "w")
file_Umur = open("Umur.txt", "w")
file_NamaUmur = open("NamaUmur.txt", "w")

#Access mode
file_Nama.write(str(kum_nama))
file_Umur.write(str(kum_umur))
for i in range(5):
    Nama_Umur = []
    Nama_Umur.append(kum_nama[i] + " " + str(kum_umur[i]))
    file_NamaUmur.write(str(Nama_Umur)+ "\n")
