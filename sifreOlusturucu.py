import random

bHarf = "QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ"

kHarf = "qwertyuıopğüasdfghjklşizxcvbnmöç"

sayilar = "1234567890"

semboller = "!'+%&/()=_-/*+:;><"

hepsi = bHarf + kHarf + sayilar + semboller

uzunluk = 15

sifre = "".join(random.sample(hepsi, uzunluk))

print(sifre)