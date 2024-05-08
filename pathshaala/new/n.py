import csv
import random
import os
import datetime
# import code128
from PIL import Image, ImageDraw, ImageFont
# name = "Heet surana"
# number= "9373758911"
# roll= "24V001"
# classs= "1"
with open("2.csv","r") as dataframe:
    data = csv.reader(dataframe)
    for line in data :
        n1=line[1]
        n2=line[2]
        name = n1[0].upper()+n1[1:].lower()+" "+n2[0].upper()+n2[1:].lower()
        number = line[3]
        roll = line[0]
        classs = line[4]
        print(name,number,roll)
        image = Image.open("1.png")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("ADLaMDisplay-Regular.ttf", 55)
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
        draw.text((x, y), str("24V"+roll[-3:]), fill=color, font=font)

        (x, y) = (280, 785)
        # classs = input('Enter Your class: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), classs, fill=color, font=font)

        # save the edited image

        image.save(str(roll) + '.png')
        import qrcode
        img = qrcode.make(roll)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        til = Image.open(roll + '.png')
        til.paste(img, (200, 810))
        til.save(roll + '.png')





