from instabot import Bot
#pip install Instabot

bot = Bot()

#hesap bilgileriniz
bot.login(username = "kullanıcıadı",
password = "parola")

bot.upload_photo("YazılımaKodluyorumYeni.jpg",
#yüklemek istediğiniz fotoğraf 
caption ="Açıklama kısmına yazılacaklar")