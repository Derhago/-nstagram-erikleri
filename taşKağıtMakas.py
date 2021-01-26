import random
"""
Taş Makası alır
Kağıt Taşı alır
Makas Kağıtı alır
Birbirine eşitse berabere
"""
hak = int(input("Kaç defa oynamak istiyorsun: "))


while hak:
    hak -= 1
    
    oyuncu = input("taş/kağıt/makas: ")
    bilgisayar = random.choice(["taş","kağıt","makas"])
    
    if oyuncu == bilgisayar:
        print("Berabere")
        
    elif oyuncu == "taş":
        if bilgisayar == "kağıt":
            print("Kazandınız.")
        else:
            print("Bilgisayar kazandı.")
            
    elif oyuncu == "kağıt":
        if bilgisayar == "taş":
            print("Kazandınız.")
        else:
            print("Bilgisayar kazandı.")
            
    elif oyuncu == "makas":
        if bilgisayar == "kağıt":
            print("Kazandınız")
        else:
            print("Bilgisayar kazandı")
            
    else:
        print("3 seçeneğin var unutma!")
    if hak == 0:
        print("Oyun bitmiştir")