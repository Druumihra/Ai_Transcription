from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def addSubtitle(srtfile, videofile): 
    generator = lambda txt: TextClip(txt, font='Arial', fontsize=36, color='white')
    subtitles = SubtitlesClip(srtfile, generator).add_mask()

    video = VideoFileClip(videofile)
    result = CompositeVideoClip([video, subtitles.set_pos(('center', 950))])

    result.write_videofile("out.mp4", fps=video.fps, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

