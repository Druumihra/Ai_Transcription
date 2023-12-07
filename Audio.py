from moviepy.editor import *
import os

def Mp4ToMp3(video):
    mp4file = VideoFileClip(video)
    video = video.strip(".mp4")
    mp3file = mp4file.audio.write_audiofile('%s-audio.wav'%(video))
    return mp3file