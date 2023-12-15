import whispertranscribe
import Audio
import Subtitle
import os



os.remove("Files/test.srt")
audio = Audio.Mp4ToMp3("Files/videofile.mp4")
whispertranscribe.whisperSTT(audio)
Subtitle.addSubtitle("Files/test.srt","Files/videofile.mp4")

