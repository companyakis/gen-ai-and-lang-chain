youtube_audio = open("/content/BİRLEŞİK KRALLIK VE İNGİLTERE 'NİN FARKI - GENEL KÜLTÜR.mp3", "rb")

transcript = client.audio.transcriptions.create(
    model = "whisper-1",
    file = youtube_audio
)

print(transcript.text)

"""
Birleşik Krallık'la İngiltere'nin farkı nedir? Bu gördüğünüz ülkelerin hepsi Birleşik Krallık. 
İngiltere, kendi bayrağı bu. Galler, kendi bayrağı bu. İskoçya'nın bayrağı bu. 
Ve aynı zamanda da Kuzey İrlanda, güneyle karıştırmayın bayrağı bu. 
Kuzey İrlanda'yı çıkartırsanız buna Büyük Britanya diyoruz, bayrağı bu. 
Eğer Kuzey İrlanda'yı katarsak Birleşik Krallık deniyor, United Kingdom. 
Ve bu bayrakların oluşumu hepsini birleştirince İrlanda'nın eski bayrağıyla Büyük Britanya bayrağını ortaya çıkarıyor. 
Lakin tamamına Güney İrlanda dahil Britanya adaları diyoruz. Peki kraliçe hangisinin başında? Hangisini yönetiyordu? 
Ya da ondan sonra gelen kral? Hepsini ve 54 ülke dahil daha fazlasını. 
Çünkü İngiliz Milletler Topluğu denilen Büyük 54 ülkeden, 1900 yılından beri bir araya gelen 54 ülkeden oluşan bir oluşumun başında aslında kraliçe.

"""
