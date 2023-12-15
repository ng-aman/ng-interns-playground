import json
import csv
import os

def is_person_json(filename):
    return filename.lower().startswith("person") and filename.endswith(".json")

def process_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            
            if is_person_json(os.path.basename(file_path)):
                data['age'] = data.get('age', 'MISSING')
                data['occupation'] = data.get('occupation', 'MISSING')
                data['salary'] = data.get('salary', 'MISSING')
                data['phone_number'] = data.get('phone_number', 'MISSING')
                
                return data
            else:
                print(f"Skipping non-person JSON file: {file_path}")
                return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in file {file_path}: {e}")
        return None

def process_folder(folder_path):
    processed_data = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and is_person_json(filename):
            processed_data.append(process_json_file(file_path))

    assert processed_data, "No valid person data to write to CSV."

    output_csv_path = os.path.join(folder_path, 'output.csv')
    try:
        with open(output_csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'age', 'occupation', 'salary', 'phone_number'])
            csv_writer.writeheader()
            csv_writer.writerows(filter(None, processed_data))
        print(f"CSV file successfully created at {output_csv_path}")
    except Exception as e:
        assert False, f"Error writing to CSV file: {e}"

# Replace 'your_folder_path' with the actual path to your folder
process_folder(r'C:\Users\MsK_PC\ng-interns-playground\submissions\satish\json_files')
