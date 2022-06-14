# orang = ["otong", "ucup", "dodit"]
# for i in orang:
#     print(i)

# for i in orang:
#     print(orang)
# print("\n")

# nama = "gesyareihan"
# for karakter in nama:
#     print(karakter)
# for karakter in nama:
#     print(nama)
    

# jumlah = int(input("Masukkan jumlah perulangan : "))
# listangka = []

# for i in range(jumlah):
#     angka = int(input("Masukkan angka : "))
#     listangka.append(angka)

# total = sum(listangka)/len(listangka)
# print(total)



# username = "gesyareihan"
# password = "nurbayan"
# i = 0
# while i <= 3:
#     us = input("Masukkan username : ")
#     ps = input("Masukkan password : ")
#     i += 1
#     if us == "gesyareihan" and ps == "nurbayan":
#         print("anda berhasil login")
#         break
#     else:
#         print("anda gagal masuk, silahkan coba lagi")



def tanah(panjangtanah, lebartanah):
    panjangtanah = float(panjangtanah)
    lebartanah = float(lebartanah)
    def luastanah(panjangtanah, lebartanah):
        return panjangtanah*lebartanah

    def kelilingtanah(panjangtanah, lebartanah):
        return 2*(panjangtanah+lebartanah)

    print("Jadi luas tanahnya adalah", luastanah(panjangtanah, lebartanah))
    print("Jadi keliling tanahnya adalah", kelilingtanah(panjangtanah, lebartanah))

panjangtanah = int(input("masukkan panjang tanah : "))
lebartanah = int(input("masukkan lebar tanah : "))

tanah(panjangtanah, lebartanah)