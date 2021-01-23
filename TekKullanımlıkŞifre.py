import random
numaralar = '1234567890'
print("4 haneli parola oluşturmak istiyorsanız 1 girin")
print("6 haneli parola oluşturmak istiyorsanız 2 girin")
rakamlar = int(input("1 veya 2 giriniz: "))
if rakamlar == 1:
    tek = random.choices(numaralar, k = 4)
    sifre=''.join(tek)
    print(sifre)
elif rakamlar == 2:
    tek = random.choices(numaralar, k = 6)
    sifre=''.join(tek)
    print(sifre)
else:
    print("Yalnızca 1 veya 2 girebilirsiniz")