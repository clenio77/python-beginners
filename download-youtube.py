import yt_dlp


#Entre com a url para o download
url = input("Insira a URL do video: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    
print("Video download com Sucesso!")    
