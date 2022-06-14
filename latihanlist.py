lista = [10,25,13,24,15,25,25,35,6,35,8,35]
print(lista)

#mengambil index
print(lista[2:4])

#sort = mengurutkan
lista.sort()
print(lista)

#reverse = membalikkan urutan
lista.reverse()
print(lista)

#append = menambahkan
lista.append(30)
print(lista)

#insert = menambahkan di index berapa
lista.insert(0,40)
print(lista)

#pop = menghapus index ke berapa
lista.pop()
print(lista)

#remove = menghapus datanya
lista.remove(10)
print(lista)

#extend = menambahkan list dalam list
lista.extend([40,50,60])
print(lista)

#index => nyari data tersebut index ke berapa
print(lista.index(60))

#count = menghitung data tersebut ada berapa
print(lista.count(25))

#clear = menghapus semua anggota list
lista.clear()
print(lista)
