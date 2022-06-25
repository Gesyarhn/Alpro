# import library yang dibutuhkan
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

jumlah_tebak = 10
while True:
    try:
        angka = int(input("Masukkan jumlah tebak: "))
        if angka != jumlah_tebak:
            print("jumlah tebak tidak sesuai")
        elif angka == jumlah_tebak:
            print("Game dimulai")
            break
    except ValueError:
        print("Masukkan angka yang bulat!")
        
# membuat jendela GUI
window=Tk()
window.title("Hangman")

# daftar hewan yang akan muncul secara acak
daftar_kata = ["MONKEY", "LION", "PANDA", "TIGER", "DOG", "CAT", "RABBIT", "MOUSE",]

# kumpulan step-step gambar yang akan muncul jika salah tebak huruf
foto = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

# fungsi untuk memulai game baru
def gamebaru():
    messagebox.showinfo("Hangman", "Its The Animal Name")
    global kata_dengan_spasi
    global jumlahtebak
    jumlahtebak=0
    imgLabel.config(image=foto[0])
    hewan=random.choice(daftar_kata)
    kata_dengan_spasi=" ".join(hewan)
    lblWord.set(" ".join("_"*len(hewan)))
    
# fungsi utama game hangman untuk menebak huruf
def game(isi):
    global jumlahtebak
    if jumlahtebak<11:
        teks=list(kata_dengan_spasi)
        tebak=list(lblWord.get())
        if kata_dengan_spasi.count(isi)>0:
            for c in range(len(teks)):
                if teks[c]==isi:
                    tebak[c]=isi
                lblWord.set("".join(tebak))
                if lblWord.get()==kata_dengan_spasi:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    gamebaru()
        else:
                jumlahtebak+=1
                imgLabel.config(image=foto[jumlahtebak])
                if jumlahtebak==11:
                 messagebox.showwarning("Hangman", "Game Over")

# insialisasi class tkinter
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
imgLabel.config(image=foto[0])
lblWord=StringVar()

# membuat label untuk menampilkan kata
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n=0

# looping untuk membuat tombol huruf
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: game(c), font=("Helvetica 18"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

# membuat tombol untuk merestart game
Button(window, text="new\nGame", command=lambda:gamebaru(),font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

gamebaru()    
window.mainloop()
