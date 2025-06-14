import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # Try "medium" or "large" for higher quality
    result = model.transcribe(audio_path)
    return result['text']
