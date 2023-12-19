import pandas as pd
import glob
import os

# Specify the path to the directory containing JSON files
json_files_path = 'C:\\Users\\DELL\\projectfile\\file_data\\'

# Use glob to get a list of all JSON files in the directory
json_files = glob.glob(f'{json_files_path}*.json')

# Check if any JSON files were found
if not json_files:
    raise FileNotFoundError("No JSON files found in the specified directory.")

# Read all JSON files into a single DataFrame
dfs = [pd.read_json(file, encoding='UTF-8', lines=True) for file in json_files]

# Combine DataFrames
df = pd.concat(dfs, ignore_index=True)

# Change JSON file paths to use a single forward slash
df['file_path'] = df['file_path'].str.replace(os.path.sep, '/')

# Save the combined DataFrame to an Excel file
excel_output_path = 'combined_output.xlsx'
df.to_excel(excel_output_path, index=False)
print(f"DataFrame saved to Excel file: {excel_output_path}")

# Save the combined DataFrame to a CSV file
csv_output_path = 'combined_output.csv'
df.to_csv(csv_output_path, index=False)
print(f"DataFrame saved to CSV file: {csv_output_path}")
