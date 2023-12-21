import whispertranscribe
import Audio
import Subtitle
import os


language = ["ca", "en", "es"]
i = 0
audio = Audio.Mp4ToMp3("Files/videofile.mp4")
for lang in language:
    if os.path.isfile(f"Files/{lang}-transcription.srt"):
        os.remove(f"Files/{lang}-transcription.srt")
    print(f"starting transcription for {lang}")
    whispertranscribe.whisperSTT(audio, lang)
    print(f"transcription done for {lang}")
    if lang == "en":
        Subtitle.addSubtitle("Files/en-transcription.srt","Files/videofile.mp4", lang)
    i+1

