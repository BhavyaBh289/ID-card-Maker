import pandas as pd

# Step 1: Read the CSV file
input_file = '2.csv'  # Replace with your input CSV file path
df = pd.read_csv(input_file)

column_name = df.columns[1]
df_cleaned = df.drop_duplicates(subset=[column_name])

# Step 3: Save the cleaned DataFrame back to a new CSV file
output_file = 'output.csv'  # Replace with your desired output CSV file path
df_cleaned.to_csv(output_file, index=False)

print(f"Removed duplicates and saved the cleaned data to {output_file}")
