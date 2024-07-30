import cv2
import numpy as np
# Carrega a imagem
image = cv2.imread('aula.jpeg')
# Converte a imagem para o espaço de cores HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# Aumenta a saturação da imagem
hsv[:, :, 1] = hsv[:, :, 1] * 1.5
# Converte a imagem de volta para o espaço de cores BGR
image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
# Salva a imagem
cv2.imwrite('image_enhanced.jpg', image)