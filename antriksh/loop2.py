import csv
import random
import os
import datetime
import code128
from PIL import Image, ImageDraw, ImageFont

with open("2.csv","r") as dataframe:
    data = csv.reader(dataframe)
    for line in data :
        name = line[1]
        name=name.center(30)
        image = Image.open("unnamed.jpg")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("NimbusMonoPS-Regular.otf", 30)
        # font = ImageFont.load_default()
        (x, y) = (185, 280)
        # name = input('Enter Your Full Name: ')
        color = 'rgb(256, 256, 256)'  # black color
        # font = ImageFont.load_default()
        draw.text((x, y), name, fill=color, font=font)
        image.paste(code128.image(line[0]), (0, 0))

        image.save(str(line[0]) + '.png')





