from pylibdmtx.pylibdmtx import encode, decode
from PIL import Image
import cv2
import pandas as pd

data = '010896110309001021bLvYaQkH7ZHxI91UZF092QWtVZRxqLgVm5yQbXGVUgDvPkcYYWOSkGjrOf0NB0Xc='
data = data.replace('', '')
data = data.replace(' ', '')
encoded = encode(data.encode('utf8'))

img = Image.frombytes('RGB', (encoded.width, encoded.height), encoded.pixels)
img.save('dmtx.png')
img = cv2.imread('dmtx.png')

decoded_data = decode(img)[0]
decoded = decoded_data[0]

Dict = {
    'Global Trade Item Number (GTIN)' : decoded[2:16].decode('utf-8'),
    'Serial Number' : decoded[18:31].decode('utf-8'),
    'Company Internal Info' : decoded[33:37].decode('utf-8'),
    'Company Internal Info Hash' : decoded[39:].decode('utf-8')
}

print('---------------------------------')
for keys, value in Dict.items():
    print(f'{keys}: {value}')
print('---------------------------------')