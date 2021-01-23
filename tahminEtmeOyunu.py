import random
print("TAHMİN ETME OYUNU")
sayi = random.randint(1, 100)

hak = int(input("Kaç hak istersiniz: "))
while hak>0:
    hak -=1
    tahmin = int(input("Tahmininizi giriniz: "))
    
    if sayi == tahmin:
        print("Doğru tahmin bravo")
        break
    elif sayi > tahmin:
        print("Biraz daha yukarı çık")
    else:
        print("Biraz daha aşağı in")
else:
    print(f"Tahmin hakkınız bitmiştir.Sayı ise {sayi}")