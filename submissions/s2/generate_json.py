import os 
import json
from datetime import datetime 
from tqdm import tqdm 
import time 
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import argparse

# Function to create json files
def create_json_files(sub_dir, num_files):
    current_datetime = datetime.now()
    for i in tqdm(range(1, num_files + 1), desc="Generating JSON files", unit="file"):
        file_name = f'json_file_{i}.json'
        json_file_path = os.path.join(sub_dir, file_name)
        
        json_file_data = {           
            "year": current_datetime.year,
            "month": current_datetime.month,
            "day": current_datetime.day,
            "timestamp": current_datetime.isoformat(), 
            "file_name": file_name,
            "file_path": json_file_path
        }

        with open(json_file_path, "w") as files:
            files.write(json.dumps(json_file_data))

# Function to read a single json file
def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

# Function to read all json files using multiprocessing
def read_all_json_files(folder_path, num_cores):
    json_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".json")]

    with ProcessPoolExecutor(max_workers=num_cores) as executor, tqdm(total=len(json_files), desc="Reading JSON files", unit="file") as pbar:
        results = list(executor.map(read_json_file, json_files))
        pbar.update(len(results))

    return results

# Function to create dataframe and save as CSV
def create_dataframe_and_csv(sub_dir, csv_filename, num_cores, num_files):
    start_time = datetime.now()

    create_json_files(sub_dir, num_files)
    json_data_list = read_all_json_files(sub_dir, num_cores)

    df = pd.DataFrame(json_data_list)
    df.to_csv(csv_filename, index=False)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time.total_seconds():.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate JSON files, read them, and save as CSV.')
    parser.add_argument('--cores', type=int, default=os.cpu_count(), help='Number of cores to use for multiprocessing.')
    parser.add_argument('--num_files', type=int, default=100000, help='Number of JSON files to generate.')
    args = parser.parse_args()

    # Storing current directory path
    curr_dir = os.getcwd()
    # Joining new directory into the current directory
    sub_dir = os.path.join(curr_dir, "json_data")

    # Checking previous existence of the same (new) directory 
    if not os.path.exists(sub_dir):
        os.mkdir(sub_dir)
        print("Successfully created sub_directory to generate json files")

    # Specify the CSV filename
    csv_filename = "output_data.csv"

    create_dataframe_and_csv(sub_dir, csv_filename, args.cores, args.num_files)
