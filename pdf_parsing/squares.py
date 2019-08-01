from PIL import Image
import os

os.mkdir('squares')

for path in os.listdir('out'):
    image = Image.open(f'out/{path}')
    width, height = image.size
    if width * .8 < height < width * 1.2:
        os.rename(f'out/{path}', f'squares/{path}')

