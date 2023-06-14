import pandas as pd
import pdfkit
from datetime import datetime, timedelta
import code128
import random

#generate costum html file using the arguments
def HTMLgen(code,first_name,last_name,function,date_of_birth,picture,expiration_date):
    html= r"""<!doctype html><meta charset="utf-8"><link rel="stylesheet" href="../RES/card.css"><body><div class="face face-front" ><img src="../RES/front.png"></div><div id="infoi"><img src="@picture" height="89.5" width="83" />
        <div style="margin-left: 1.3cm;margin-top: -0.6cm;">
            <br>
            <div style="font-size: 0.7em;margin-top: 5%;font-family: sans-serif;color: aliceblue;text-transform: uppercase;"><b>@fname</b> @lname</div><br>
        <div style="font-size: 0.7em;margin-top: -0.4cm;font-family: sans-serif;color: aliceblue;text-t ransform: capitalize;">@function</div>
        </div>
    </div>
    <div id="info">
        <br><div style="font-size: 0.7em;margin-top: 0.6%;font-family: sans-serif;text-transform: uppercase;">@code</div>
        <br><div style="font-size: 0.7em;margin-top: -0.6%;font-family: sans-serif;text-transform: capitalize;">@date_of_birth</div>
        <br><div style="font-size: 0.7em;margin-top: -0.6%;font-family: sans-serif;text-transform: capitalize;">@expiration_date</div>
    </div>
    <div id="BARCODE"><img src="../RES/bar.PNG"  height="20" width="120"/></div>

</body>"""
    html = html.replace("@picture",picture)
    html = html.replace("@code",str(code))
    html = html.replace("@fname",first_name)
    html = html.replace("@lname",last_name)
    html = html.replace("@function",function)
    html = html.replace("@date_of_birth",date_of_birth)
    html = html.replace("@expiration_date",expiration_date)
    f= open("index.html","w")
    f.write(html)
    f.close()
    return
#generate a file bar.png contains barcode of the 10 digits code
def BARgen(code):
    code128.image(code).save("../RES/bar.png")
    return
#generate costum pdf file using the existing html file // code argument is only to name the file generated
def PDFgen(code):
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    options = {'dpi': 365,'margin-top': '0in','margin-bottom': '0in','margin-right': '0in','margin-left': '0in','page-size': 'A8',"orientation": "Landscape",'disable-smart-shrinking': ''}
    pdfkit.from_file('index.html', str(code)+".pdf",configuration=config , options = options)
    return
#complete with random digits an integer x until it contains 10 digits
def complete(x):
    x=str(x)
    while len(x)<10:
            x+=str(random.randint(0,9))
    return int(x)
data=pd.read_excel("../.xlsx")
