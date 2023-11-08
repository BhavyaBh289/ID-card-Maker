import csv
import random
import os
import datetime
import code128
from PIL import Image, ImageDraw, ImageFont
from matplotlib import font_manager
import img2pdf
with open("2.csv","r") as dataframe:
    data = csv.reader(dataframe)
    for line in data :
        name = line[1]
        name=name.center(30)
        image = Image.open("unnamed.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Bell MT.ttf", 30)
        # font = ImageFont.load_default()
        (x, y) = (280, 280)
        # name = input('Enter Your Full Name: ')
        color = 'rgb(256, 256, 256)'  # black color
        # font = ImageFont.load_default()
        draw.text((x, y), name, fill=color, font=font)
        image.save(str(line[0]) + '.png')
        imagee = Image.open(str(line[0]) + '.png')
        pdf_bytes = img2pdf.convert(imagee.filename)
        with open(str(line[0]) + '.pdf', 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)





