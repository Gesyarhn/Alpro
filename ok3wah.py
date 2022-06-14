print("Himpunan")

set_a = {0,1,2,3,4,5,6,7,8,9,10}
set_b = {6,7,8,9,10,11,12,13,14,15}
set_c = {16,17,18,19,20}



print(""" 
1. Menggabungkan 2 set (union)
2. Irisan 2 set (intersection)
3. selisih 2 set (difference)
4. New Set (Update)
0. exit
""")

while True:
    kode = int(input("Masukkan kode menu yang anda inginkan : "))
    if kode == 1:
        sethasil = set_a.union(set_b)
        print(sethasil)
    elif kode == 2:
        setinter = set_a.intersection(set_b)
        print(setinter)
    elif kode == 3:
        setdiff = set_a.difference(set_b)
        print(setdiff)
    elif kode == 4:
        set_c.update(sethasil)
        print(set_c)
    elif kode >= 5:
        print("Anda hanya bisa memilih sampai nomor 4")
    elif kode == 0:
        break


