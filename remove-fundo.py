from rembg import remove
from PIL import Image

entrada = 'arlequina.jpg'
saida = 'arlequina.png'

inp = Image.open(entrada)
output = remove(inp)
output.save(saida)