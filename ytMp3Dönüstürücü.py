import pafy
#pip install pafy
#pip install youtube-dl

url = input("Youtube Url Giriniz: ")

video = pafy.new(url)

audios = video.getbestaudio()
audios.download()
