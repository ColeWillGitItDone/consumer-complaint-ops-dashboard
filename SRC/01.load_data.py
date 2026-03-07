import pandas as pd

file_path = "Data/01. raw/complaints.csv"

df = pd.read_csv(file_path)

print("Rows and Columns:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())