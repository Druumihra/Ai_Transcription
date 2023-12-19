import whispertranscribe
import Audio
import Subtitle
import os
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


language = ["ca", "en", "es"]
i = 0
audio = Audio.Mp4ToMp3("Files/videofile.mp4")
for lang in language:
    whispertranscribe.whisperSTT(audio, lang)
    Subtitle.addSubtitle("Files/test.srt","Files/videofile.mp4", lang)
    
    i+1

