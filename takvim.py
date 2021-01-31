import calendar
import locale  #dili değiştirdik
locale.setlocale(locale.LC_ALL, "tr_TR.utf8")

yil = int(input("Bir Yıl Giriniz: "))
ay = int(input("Bir Ay Giriniz: "))


print(calendar.month(yil, ay))