import whispertranscribe
import Audio
import Subtitle



language = ["ca", "en", "es"]
i = 0
audio = Audio.Mp4ToMp3("Files/videofile.mp4")
for lang in language:
    whispertranscribe.whisperSTT(audio, lang)
    if language == "en":
        Subtitle.addSubtitle("Files/en-transcribtion.srt","Files/videofile.mp4", lang)
    i+1

