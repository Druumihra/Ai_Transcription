import whisper

def whisperSTT(audio):
    model = whisper.load_model("base")
    result = model.transcribe(audio)
    print(result["text"])