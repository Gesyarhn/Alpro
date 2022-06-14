kata = input("Masukkan kata : ")
tuple1 = tuple(kata)
print(tuple1)
print()

print("""Menu tuple
1. jumlah huruf
2. membalik urutan
3. menghapus huruf pertama""")

jumlah = int(input("Jumlah aktivitas yang kamu inginkan : "))

for i in range(jumlah):
    kode = int(input("Masukkan kode menu : "))
    if kode == 1:
        print("Jumlah huruf dari tuple adalah : ", len(tuple1))
    elif kode == 2:
        print("Hasil membalikkan urutan : ", tuple1[::-1])
    elif kode == 3:
        x = list(tuple1)
        x.pop(0)
        tuple1 = tuple(x)
        print("Hasil menghapus huruf pertama:", tuple1)
