from PIL import Image
#pip install Pillow

foto = Image.open("Yazılıma Kodluyorum.png")

siyahBeyaz = foto.convert("L")

siyahBeyaz.save("YazılımaKodluyorumYeni.jpg")

siyahBeyaz.show()