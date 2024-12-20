import pandas as pd

file_path = './IMDB_Movies.xlsx'
excel_data = pd.ExcelFile(file_path)

excel_data.sheet_names
movies_data = excel_data.parse('IMDB_Movies')

movies_data_1NF = movies_data.copy()

movies_data_1NF = movies_data_1NF.dropna(subset=['genres'])
movies_data_1NF = movies_data_1NF.assign(genres=movies_data_1NF['genres'].str.split(','))
movies_data_1NF = movies_data_1NF.explode('genres').reset_index(drop=True)

print(movies_data_1NF.head())
output_path = './IMDB_Movies_1NF.xlsx'
movies_data_1NF.to_excel(output_path, index=False)
print(f"File saved successfully to {output_path}")
