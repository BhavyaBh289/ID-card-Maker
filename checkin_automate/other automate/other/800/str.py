 
import csv

# Read data from the CSV file
data_rows = []
with open('1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_reader)  # Read the headers
    for row in csv_reader:
        data_rows.append(row)

# Remove leading numbers from the first row
for i in range(len(data_rows)):
    while data_rows[i][0][0].isdigit():
        data_rows[i][0]=data_rows[i][0][1:]
print("Headers:")
print(", ".join(headers))

# Print the data in a simple format
print("Data:")
for row in data_rows:
    print(row[0])
