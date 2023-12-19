import json
import os
import pandas as pd
import argparse
import logging
from tqdm import tqdm
from datetime import datetime

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_json_file(json_file_path):
    try:
        # Read JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Ensure the data is a dictionary
        assert isinstance(data, dict), f"Invalid JSON format in file - {json_file_path}"

        # Replace missing values with "MISSING"
        data['name'] = data.get('name', 'MISSING')
        data['age'] = data.get('age', 'MISSING')
        data['occupation'] = data.get('occupation', 'MISSING')
        data['salary'] = data.get('salary', 'MISSING')
        data['phone_number'] = data.get('phone_number', 'MISSING')

        return data
            
    except json.JSONDecodeError:
        logger.error(f"Error: Invalid JSON format - {json_file_path}")
        return None
    except Exception as e:
        logger.error(f"Error: {e} - {json_file_path}")
        return None

def process_json_folder(json_folder, csv_output_path):
    # Initialize an empty list to store data from all JSON files
    all_data = []

    # Loop through each JSON file
    for json_file in tqdm(os.listdir(json_folder), desc="Processing JSON files", unit="file"):
        if json_file.startswith("person_") and json_file.endswith(".json"):
            json_file_path = os.path.join(json_folder, json_file)
            data = process_json_file(json_file_path)

            if data is not None:
                all_data.append(data)

    # Create DataFrame
    df = pd.DataFrame(all_data)

    # Save DataFrame to CSV
    df.to_csv(csv_output_path, index=False)

    logging.info(f"Processing completed. Results saved to {csv_output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process JSON files and save results to CSV.')
    parser.add_argument('--json_folder', required=True, help='Path to the folder containing JSON files.')
    parser.add_argument('--csv_output', required=True, help='Path for the output CSV file.')
    args = parser.parse_args()

    # Storing start time
    start_time = datetime.now()

    # Set up tqdm bar
    tqdm_bar = tqdm(total=len(os.listdir(args.json_folder)), desc="Total Progress", unit="file")

    # Process JSON folder and save to CSV
    process_json_folder(args.json_folder, args.csv_output)

    # Close tqdm bar
    tqdm_bar.close()

    # Calculate and log the elapsed time
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    logging.info(f"Total time taken: {elapsed_time.total_seconds():.2f} seconds")
