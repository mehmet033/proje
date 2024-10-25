import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
isim = input("Adınızı girin: ")
plaka_numarasi = input("Yaşadığınız şehrin plaka numarasını girin: ")
yas = input("Yaşınızı girin: ")
uzunluk = int(input("Parolanın uzunluğunu girin: "))
parola = ""

while True:
    parola = ""
    for _ in range(uzunluk):
        parola += random.choice(karakterler)
    
    if isim not in parola and plaka_numarasi not in parola and yas not in parola:
        break

print("Oluşturulan parola: ", parola)