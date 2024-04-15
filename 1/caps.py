import csv
with open("1.csv","r") as file1:
    with open("2.csv","w") as file2:
        # while
        file2.writelines(file1.read().upper())
