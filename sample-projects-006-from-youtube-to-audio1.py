from pytubefix import YouTube

from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/shorts/5iWkA8t-8D8"
 
yt = YouTube(url, on_progress_callback = on_progress)

print(yt.title)
 
ys = yt.streams.get_audio_only()

ys.download(mp3=True)

# BİRLEŞİK KRALLIK VE İNGİLTERE 'NİN FARKI - GENEL KÜLTÜR
# /content/BİRLEŞİK KRALLIK VE İNGİLTERE 'NİN FARKI - GENEL KÜLTÜR.mp3