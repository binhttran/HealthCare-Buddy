import os

# Path to the directory where the dataset is saved
dataset_dir = "predicting-heart-disease-risk-using-clinical-var"

# List all files in the directory
files = os.listdir(dataset_dir)
print("Files in the dataset directory:", files)

import pandas as pd

# Choose a file to read (e.g., the first CSV file in the directory)
csv_file = os.path.join(dataset_dir, files[0])  # Adjust index if needed

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file)

# Display the first few rows of the dataset
# print(df.head())
#check for missing values

print(df.describe())  # Summary statistics
print(df.info())      # Dataset structure and data types



