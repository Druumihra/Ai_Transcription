import whispertranscribe
import Audio


audio = Audio.Mp4ToMp3("Video/5Histo60s_EDIT.mp4")
whispertranscribe.whisperSTT(audio)


