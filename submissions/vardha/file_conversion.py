import pandas as pd
import glob

# Path of directory containing JSON files
file_path = "C:\\Users\\vardh\\OneDrive\\Desktop\\rough\\new\\ng-interns-playground\\submissions\\vardha\\output"

# Use glob to get a list of all JSON files in the directory
json_files = glob.glob(f'{file_path}*.json')

# Check if any JSON files were found
if not json_files:
    raise FileNotFoundError("No JSON files were found in the directory.")

# Read all JSON files into a single DataFrame
df = pd.concat([pd.read_json(file, encoding='UTF-8', lines=True) for file in json_files], ignore_index=True)

# Save the combined DataFrame to an Excel file
#excel_output_path = f'{file_path}\\exceloutput.xlsx'
df.to_excel("excel_output.xlsx", index=False)

# Save the combined DataFrame to a CSV file
#csv_output_path = f'{file_path}\\csvoutput.csv'
df.to_csv("csv_output.csv", index=False)