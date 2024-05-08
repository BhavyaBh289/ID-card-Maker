import csv
import random
import os
import datetime
# import code128
from PIL import Image, ImageDraw, ImageFont

# with open("2.csv","r") as dataframe:
#     data = csv.reader(dataframe)
#     for line in data :
        # name = line[0]
        # number = line[1]
        # roll = line[2]
        # classs = line[3]
        # print(name,number,roll)
name = "Heet surana"
number= "9373758911"
roll= "24V001"
classs= "1"
image = Image.open("1.png")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("ADLaMDisplay-Regular.ttf", 60)
# font = ImageFont.load_default()
(x, y) = (70, 560)
# name = input('Enter Your Full Name: ')
color = 'rgb(0, 0, 128)'  # black color
# font = ImageFont.load_default()
W=image.width
# print(W)
_, _, w, h = draw.textbbox((0, 0), name, font=font)
draw.text(((W-w)/2, y), name, fill=color, font=font)

font = ImageFont.truetype("NimbusMonoPS-Regular.otf", 40)
(x, y) = (280, 680)
# number = input('Enter Your Mobile Number: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), number, fill=color, font=font)

(x, y) = (280, 732)
# roll = input('Enter Your roll number ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), roll, fill=color, font=font)

(x, y) = (280, 785)
# classs = input('Enter Your class: ')
color = 'rgb(0, 0, 0)'  # black color
draw.text((x, y), classs, fill=color, font=font)

# save the edited image

image.save(str(roll) + '.png')

# til = Image.open(roll + '.png')
# til.paste(code128.image(roll), (650, 440))
# til.save(roll + '.png')





