import os
import urllib.request

# Ask for the url of the video
url = input("Insira a url do video: ")

# Ask for the video name
name = input("Digite o nome do arquivo (inclua a extensão): ")

# Save the video in the same directory as the script
dest = os.path.dirname(os.path.abspath(__file__))

# Save the video in the specified directory
full_path = os.path.join(dest, name)

# Download the video
urllib.request.urlretrieve(url, full_path)

print("Download concluído.")