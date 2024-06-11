import re
import csv
f=open("Text File (9).txt","r")
data = f.read()
# Split the data into lines
lines = data.strip().split('\n')

# Create a list to hold the parsed data
parsed_data = []
current_entry = []
row1=[]
row2=[]
ce2=[]
Address=[]
headers = ["Name", "Address", "Postal Code", "Email 1", "Email 2", "Telephone 1", "Telephone 2","Telephone 3"]
t=0
for i, line in enumerate(lines):
    if t==0:
        current_entry.append(line.strip())
        t=1
    elif t ==-1:
        row2.append(ce2)
        ce2=[]
        t=0
    elif (t==1):
        if (len(line.strip()) == 6 and line.strip().isdigit()):
            current_entry.append(Address)
            Address=[]
            current_entry.append(line.strip())
            row1.append(current_entry)
            current_entry=[]
            if(lines[i+1]=="ICAI Reg No:EMAIL"):
                t=2
            else:
                t=0
        else:
            Address.append(line.strip())
    elif (t==2):
        if(line.strip()=="ICAI Reg No:EMAIL"):
            continue
        elif(line.strip()[0]=="T"):
            ce2.append(line.strip()[-7:])
            t=3
    elif t==3:                                #email1
        if('@' in line.strip()):
            ce2.append(line.strip())
            t=4
        else:
            ce2.append("")
            t=4
    elif t==4:                                #email1
        if('@' in line.strip()):
            ce2.append(line.strip())
            t=5
        elif((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
            ce2.append("")
            ce2.append(line.strip())
            t=6
    elif t==5:                                #no1
        if((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
            ce2.append(line.strip())
            t=6
        if(line.strip()=="26 September 2022"):
            ce2.append("")
            ce2.append("")
            t=-1
        if(line.strip()=="ICAI Reg No:EMAIL"):
            ce2.append("")
            ce2.append("")
            row2.append(ce2)
            ce2=[]
            t=2

    elif t==6:                                #no2
        if((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
            ce2.append(line.strip())
            t=7
        if(line.strip()=="26 September 2022"):
            ce2.append("")
            t=-1
        if(line.strip()=="ICAI Reg No:EMAIL"):
            ce2.append("")
            row2.append(ce2)
            ce2=[]
            t=2
    elif t==7:                                #no3
        if((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
            ce2.append(line.strip())
        if(line.strip()=="26 September 2022"):
            t=-1
        if(line.strip()=="ICAI Reg No:EMAIL"):
            row2.append(ce2)
            ce2=[]
            t=2
    elif(line.strip()=="26 September 2022"):
        t=-1
    elif(line.strip()[0]=="T"):
        print(line.strip())
        ce2.append(line.strip()[-7:])
        t=3
    else:
        print(line)
print(ce2,current_entry)
print(len(row2))

import csv

with open('output4.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(headers)  # Write headers to the CSV file
    for row in row1:
        writer.writerow(row)
    for row in row2:
        writer.writerow(row)
print("CSV file created successfully!")

