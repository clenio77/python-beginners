from pydub import AudioSegment
from moviepy.editor import *

def video_to_mp3(video_file, audio_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)

video_file = "seu video"
audio_file = "output_audio.mp3"

video_to_mp3(video_file, audio_file)
