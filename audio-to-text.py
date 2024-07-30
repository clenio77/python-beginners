import speech_recognition as sr
from tkinter import filedialog
from pydub import AudioSegment
from tkinter.filedialog import askopenfilename
from  moviepy.editor import *



def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")



def transcribe_audio_file(file_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
        
    try:
        transcription = recognizer.recognize_google(audio)
        return transcription
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return None
    except sr.RequestError as e:
        print(f"Erro ao fazer a solicitação; {e}")
        return None

def open_file_and_transcribe():
    file_path = filedialog.askopenfilename()
    if file_path:
        transcription = transcribe_audio_file(file_path)
        if transcription:
            print(f"Transcrição: {transcription}")
        else:
            print("Não foi possível transcrever o áudio.")

if __name__ == "__main__":
    mp3_file_path = askopenfilename()#"path/to/your/mp3/file.mp3"
    name_arquivo = AudioFileClip(mp3_file_path)
    name = name_arquivo.filename
    wav_file_path = os.path.splitext(name)[0]
    #wav_file_path = "path/to/your/wav/file.wav"
    convert_mp3_to_wav(mp3_file_path, wav_file_path)
    open_file_and_transcribe()
        