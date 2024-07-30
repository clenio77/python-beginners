from  moviepy.editor import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import os


#read video file
video = askopenfilename()
video1 = VideoFileClip(video)

# set name video
nome_do_video = video1.filename

# set name video out extension
nome = os.path.splitext(nome_do_video)[0]

# convert video to audio
audio = video1.audio

# save audio file
audio.write_audiofile(nome+'.mp3')
