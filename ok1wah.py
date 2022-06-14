print(""" ===>>> PROGRAM WISHLIST ANIME <<<===
1. Tambahkan judul anime
2. Mengurutkan daftar anime
3. Menampilkan seluruh judul anime
0. Exit
""")

listanime = []



while True:
    kode = int(input("Masukkan kode menu yang anda inginkan : "))
    if kode == 1:
        anime =input("Masukkan judul anime : ")
        listanime.append(anime)
        print(f"{anime} sudah ditambahkan")
    elif kode == 2:
        listanime.sort()
        print("List anime sudah diurutkan!")
    elif kode == 3:
        for i in range(len(listanime)):
            print(listanime[i])
    elif kode == 0:
        print("Terima kasih telah menggunakan program kami!")
        break

        


