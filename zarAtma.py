import random

min = 1
max = 6

tekrar_atma = "evet"

while tekrar_atma == "evet" or tekrar_atma == "e":
    print("İLk Zar Atıldı")
    print(random.randint(min, max))
    print("İkinci Zar Atıldı")
    print(random.randint(min, max))
    
    tekrar_atma = input("Bir daha atmak ister misin (evet/e): ")
    