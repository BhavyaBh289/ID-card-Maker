import csv
import random
import os
import datetime
from PIL import Image, ImageDraw, ImageFont

with open("2.csv","r") as dataframe:
    data = csv.reader(dataframe)
    for line in data :
        name = line[0]
        classs = line[1][0]
        grade = line[2]
        # print(name,number,roll)

        image = Image.open("unnamed.jpg")
        draw = ImageDraw.Draw(image)


        name_font = ImageFont.truetype("/home/bh289/Documents/clg/git/ID-Cards-Generator/vatika_certifications/GreatVibes-Regular.ttf", 100)
        info_font = ImageFont.truetype("arialbi.ttf", 48)

        image_width = image.width
        name_text = name
        name_bbox = draw.textbbox((0, 0), name_text, font=name_font)
        name_width = name_bbox[2] - name_bbox[0]
        name_x = (image_width - name_width) / 2
        name_y = 535
        draw.text((name_x, name_y), name_text, fill="rgb(0, 0, 0)", font=name_font)



        (x, y) = (699, 670)
        # number = input('Enter Your Mobile Number: ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), classs, fill=color, font=info_font)

        (x, y) = (954, 670)
        # roll = input('Enter Your roll number ')
        color = 'rgb(0, 0, 0)'  # black color
        draw.text((x, y), grade, fill=color, font=info_font)

        # save the edited image

        image.save(name + '.png')





