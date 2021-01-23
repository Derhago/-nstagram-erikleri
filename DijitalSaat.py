#çağırıyoruz tkinter ve time module 
import tkinter as tk
import time


#zaman kazanmak için işlev yarat

def tick():
    time_string=time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    #Güncellenen zamanı görüntülemek için her 200 mikro saniyeden sonra tümü işaretleyin ()
    clock.after(200,tick)
    
root = tk.Tk()
root.title("Dijital Saat")
#pencerede zamanı görüntülemek için etiket oluştur

clock=tk.Label(root,font=("time",90,"bold"),bg="white")

clock.pack()

#saat etiketi için çağrı tick () işlevi

tick()

root.mainloop()
