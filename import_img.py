from cgitb import text
from tkinter import font
from PIL import Image, ImageDraw, ImageFont, ImageOps

img = Image.open('bot.png')
fonte = ImageFont.truetype('Comic Book.otf', 100)
escrever = ImageDraw.Draw(img)
escrever.text(xy=(500,500),text="Nome do membro",fill=(1000,1000,1000 ), font=fonte)
img.show()
