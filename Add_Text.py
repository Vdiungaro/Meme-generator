import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw



with open('quotes.txt', 'r') as f:
    lines = f.read().splitlines()
f.close()

selected = random.choice(lines)

# Escreve texto na imagem
img = Image.open('01.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('arial',64)
draw.text((150, 220),selected,(0,0,0),font=font,align='left')
img.save('02.jpg')