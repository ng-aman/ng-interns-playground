import json
import csv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def person_is_json(filename):
    return filename.lower().startswith("person") and filename.endswith(".json")

def process_json_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            
            if person_is_json(os.path.basename(file_path)):
                data['name'] = data.get('name', 'MISSING') 
                data['age'] = data.get('age', 'MISSING')
                data['occupation'] = data.get('occupation', 'MISSING')
                data['salary'] = data.get('salary', 'MISSING')
                data['phone_number'] = data.get('phone_number', 'MISSING')
                
                return data
            else:
                logger.info(f"Skipping non-person JSON file: {file_path}")
                return None
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON in file {file_path}: {e}")
        return None

def folder_processing(folder_path):
    processed_data = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and person_is_json(filename):
            processed_data.append(process_json_file(file_path))

    assert processed_data, "files cannot satisted the condition to CSV."

    output_csv_path = os.path.join(folder_path, 'created_csv_file.csv')
    try:
        with open(output_csv_path, 'w', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['name', 'age', 'occupation', 'salary', 'phone_number'])
            csv_writer.writeheader()
            csv_writer.writerows(filter(None, processed_data))
        logger.info(f"CSV file successfully created at {output_csv_path}")
    except Exception as e:
        logger.error(f"Error writing to CSV file: {e}")
        assert False, "Error writing to CSV file."

# giving the folder path to save the files
folder_processing(r'C:\Users\DELL\json_files\json_files')