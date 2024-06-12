import re
import csv
f=open("1.txt","r")
data = f.read()
# Split the data into lines
lines = data.strip().split('\n')

# Create a list to hold the parsed data
parsed_data = []
current_entry = []
Address=[]
headers = ["Name", "Address", "Postal Code","icie", "Email 1", "Email 2", "Telephone 1", "Telephone 2","Telephone 3"]
t=0
for i, line in enumerate(lines):
    if "ICAI Reg No:" in line :
        t=1
        current_entry.append(Address)
        Address=[]
        parsed_data.append(current_entry)
        current_entry=[]

        matcch = re.match(r'^(.*)ICAI Reg No:* (\d+[A-Z]*[a-z]*)$', line )
        current_entry.append(matcch.group(1).strip())
        current_entry.append(matcch.group(2).strip())
    elif "EMAIL" in line :
        Address=[]
        parts = line.split("EMAIL")
        Address.append(parts[0].strip())
        current_entry.append(parts[1].strip())
        t=2
    elif "Telephone" in line :
        t=3
        parts = line.split("Telephone")
        Address.append(parts[0].strip())
        current_entry.append(parts[1].strip())
    else:
        if '@'in line :
            current_entry.append(re.findall(r'[\w\.-]+@[\w\.-]+', line))
            Address.append(re.sub(r'[\w\.-]+@[\w\.-]+', '', line))
        if re.findall(r'\b\d{10,11}\b', line ):
            current_entry.append(re.findall(r'\b\d{10,11}\b', line ))
            Address.append(re.sub(r'\b\d{10,11}\b', '', line))
    # if t==0:
    #     current_entry.append(line.strip())
    #     t=1
    # elif t ==-1:
    #     row2.append(ce2)
    #     ce2=[]
    #     t=0
    # elif (t==1):
    #     if (len(line.strip()) == 6 and line.strip().isdigit()):
    #         current_entry.append(Address)
    #         Address=[]
    #         current_entry.append(line.strip())
    #         row1.append(current_entry)
    #         current_entry=[]
    #         if(lines[i+1]=="ICAI Reg No:EMAIL"):
    #             t=2
    #         else:
    #             t=0
    #     else:
    #         Address.append(line.strip())
    # elif (t==2):
    #     if(line.strip()=="ICAI Reg No:EMAIL"):
    #         continue
    #     elif(line.strip()[0]=="T"):
    #         ce2.append(line.strip()[-7:])
    #         t=3
    # elif t==3:                                #email1
    #     if('@' in line.strip()):
    #         ce2.append(line.strip())
    #         t=4
    #     else:
    #         ce2.append("")
    #         t=4
    # elif t==4:                                #email1
    #     if('@' in line.strip()):
    #         ce2.append(line.strip())
    #         t=5
    #     elif((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
    #         ce2.append("")
    #         ce2.append(line.strip())
    #         t=6
    # elif t==5:                                #no1
    #     if((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
    #         ce2.append(line.strip())
    #         t=6
    #     if(line.strip()=="26 September 2022"):
    #         ce2.append("")
    #         ce2.append("")
    #         t=-1
    #     if(line.strip()=="ICAI Reg No:EMAIL"):
    #         ce2.append("")
    #         ce2.append("")
    #         row2.append(ce2)
    #         ce2=[]
    #         t=2
    #
    # elif t==6:                                #no2
    #     if((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
    #         ce2.append(line.strip())
    #         t=7
    #     if(line.strip()=="26 September 2022"):
    #         ce2.append("")
    #         t=-1
    #     if(line.strip()=="ICAI Reg No:EMAIL"):
    #         ce2.append("")
    #         row2.append(ce2)
    #         ce2=[]
    #         t=2
    # elif t==7:                                #no3
    #     if((len(line.strip()) == 10 or len(line.strip()) == 11) and line.strip().isdigit()):
    #         ce2.append(line.strip())
    #     if(line.strip()=="26 September 2022"):
    #         t=-1
    #     if(line.strip()=="ICAI Reg No:EMAIL"):
    #         row2.append(ce2)
    #         ce2=[]
    #         t=2
    # elif(line.strip()=="26 September 2022"):
    #     t=-1
    # elif(line.strip()[0]=="T"):
    #     print(line.strip())
    #     ce2.append(line.strip()[-7:])
    #     t=3
    # else:
    #     print(line)
parsed_data.append(current_entry)
# print(parsed_data)
file_name="1.csv"
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(parsed_data)

print(f"Double array has been saved to {file_name}")
# import csv
#
# with open('output4.csv', mode='w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(headers)  # Write headers to the CSV file
#     for row in row1:
#         writer.writerow(row)
#     for row in row2:
#         writer.writerow(row)
# print("CSV file created successfully!")

