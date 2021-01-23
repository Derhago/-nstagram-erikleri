import time

def geriSayim(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1
    print('Geri Sayım Bitti', "\a")
    
t = input("Saniye cinsinden sayı giriniz: ")

geriSayim(int(t))