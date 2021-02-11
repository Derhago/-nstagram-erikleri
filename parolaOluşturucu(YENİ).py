import random
import string

def parola_uret(uzunluk, level, cikti=[]):
    karakter = string.ascii_letters
    if level > 1:
        karakter = f"{karakter}{string.digits}"
    if level > 2:
        karakter = f"{karakter}{string.punctuation}"
    
    for i in range(uzunluk):
        cikti.append(random.choice(karakter))
    
    return "".join(cikti)

print(("-" * 30) + "\n Parola Üretici\n" + ("-" * 30))

parola_uzunluk = int(input("Uzunluk: "))
parola_seviye = int(input("Seviye: "))

parola = parola_uret(parola_uzunluk, parola_seviye)
print(f"\nParolan: {parola}")