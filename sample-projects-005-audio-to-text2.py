transcript = client.audio.transcriptions.create(
    model = "whisper-1",
    file = audio_file
)

print(transcript.text) # A rolling stone gathers no moss and a barking dog never bites.



