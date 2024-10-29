response = client.audio.speech.create(
    model = "tts-1",
    voice = "nova",
    input = "A rolling stone gathers no moss and a barking dog never bites...",
    speed = 1.25
)

response.stream_to_file(sample_speech_path)
