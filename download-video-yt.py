import yt_dlp

url = input("Insira a url do video: ") #Insira o link do video aqui

def my_video(d):
    if d['status'] == 'finished':
        print('Download successfully')

yt_dlp.YoutubeDL({'format': 'best','outtmpl': '%(title)s.%(ext)s',
                  'postprocessors': [{'key': 'FFmpegVideoConvertor','preferedformat': 'mp4'}],
                  'progress_hooks': [my_video]}).download([url])