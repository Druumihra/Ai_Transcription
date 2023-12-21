import whisper
import os
from datetime import timedelta

def whisperSTT(audio, language):
    model = whisper.load_model("large-v3")
    result = model.transcribe(audio, language=language)
    segments = result["segments"]

    for segment in segments:
        startime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endtime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        id = segment['id']+1
        segment = f"{id}\n{startime} ---> {endtime}\n {text[1:] if text[0] is ' ' else text}\n\n"
        srtfilename = os.path.join("Files", f"{language}-transcription.srt")
        with open(srtfilename, 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)
    return srtfilename