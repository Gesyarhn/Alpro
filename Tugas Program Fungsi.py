#Tugas Algoritma dan Pemrograman Fungsi pada Python
print("**====Program memeriksa Palindrome====**")

def cekPalindrome(word):
    terbalik = ""
    for i in word:
        terbalik = i + terbalik
    
    x = 0
    j = 0
    for i in word:
        if i == terbalik[x]:
            j += 1

        x += 1

    if(len(word) == j):
        x = word + ", Kata ini termasuk Palindrome"
        return x
    else:
        return word[::-1]

# Cek Kata Palindrome
print(cekPalindrome("level"))
print(cekPalindrome("malam"))
print(cekPalindrome("kakak"))
print()
# Cek Kata Bukan Palindrome
print(cekPalindrome("mamah"))
print(cekPalindrome("bapak"))
print(cekPalindrome("adik"))