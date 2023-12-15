import pandas as pd
import glob

# Specify the path to the directory containing JSON files
json_files_path = 'C:\\Users\\DELL\\projectfile\\file_data\\'

# Use glob to get a list of all JSON files in the directory
json_files = glob.glob(f'{json_files_path}*.json')

# Check if any JSON files were found
if not json_files:
    raise FileNotFoundError("No JSON files found in the specified directory.")

# Read all JSON files into a single DataFrame
df = pd.concat([pd.read_json(file, encoding='UTF-8', lines=True) for file in json_files], ignore_index=True)

# Save the combined DataFrame to an Excel file
df.to_excel('exceloutput.xlsx', index=False)

# Save the combined DataFrame to a CSV file
df.to_csv('csvoutput.csv', index=False)
