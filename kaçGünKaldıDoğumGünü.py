import datetime


def başlık_yazdır():
    print('--------------------------------')
    print('    Doğum Günü Uygulaması')
    print('--------------------------------')
    print()


def kullanıcıdan_doğumgünü_bilgisini_al():
    print("Ne zaman doğdunuz? ")
    yıl = int(input("Yıl [YYYY]: "))
    ay = int(input("Ay [AA]: "))
    gün = int(input("Yıl [GG]: "))

    doğum_günü = datetime.date(yıl, ay, gün)
    return doğum_günü


def tarihler_arasındaki_günleri_hesapla(orijinal_tarih, hedef_tarih):
    bu_yıl = datetime.date(hedef_tarih.year, orijinal_tarih.month, orijinal_tarih.day)

    gün_farkı = bu_yıl - hedef_tarih
    return gün_farkı.days


def doğum_günü_bilgilerini_yazdır(günler):
    if günler < 0:
        print('Bu yıl {} gün önce doğum günün vardı.'.format(-günler))
    elif günler > 0:
        print('Doğum günün {} gün sonra!'.format(günler))
    else:
        print('Doğum günün kutlu olsun!!!')


def main():
    başlık_yazdır()
    dgünü = kullanıcıdan_doğumgünü_bilgisini_al()
    bugün = datetime.date.today()
    günlerin_sayısı = tarihler_arasındaki_günleri_hesapla(dgünü, bugün)
    doğum_günü_bilgilerini_yazdır(günlerin_sayısı)


main()