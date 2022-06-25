from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window=Tk()
window.title("Hangman")

daftar_kata = ["RAFAY", "LION", "PANDA", "TIGER", "DOG", "CAT", "RABIT", "MOUSE",]

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"),
          PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"),
          PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

def gamebaru():
    messagebox.showinfo("Hangman", "Its The Animal Name")
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    kata=random.choice(daftar_kata)
    the_word_withSpaces=" ".join(kata)
    lblWord.set(" ".join("_"*len(kata)))



def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        teks=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for x in range(len(teks)):
                if teks[x]==letter:
                    guessed[x]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    gamebaru()
        else:
                numberOfGuesses+=1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==11:
                 messagebox.showwarning("Hangman", "Game Over")
    
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text="new\nGame", command=lambda:gamebaru(),font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

gamebaru()    
window.mainloop()