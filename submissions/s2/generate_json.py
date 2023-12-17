#importing libraries 
import os 
import json
from datetime import datetime 
from tqdm import tqdm 
import time 
import pandas as pd
from concurrent.futures import ProcessPoolExecutor

#creating json files and entering data
def create_json_files(sub_dir):
    current_datetime = datetime.now()
    for i in tqdm(range(1, 100001)):
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

def read_json_file(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def read_all_json_files(folder_path):
    json_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".json")]

    with ProcessPoolExecutor() as executor, tqdm(total=len(json_files), desc="Reading JSON files", unit="file") as pbar:
        results = list(executor.map(read_json_file, json_files))
        pbar.update(len(results))

    return results

def create_dataframe_and_csv(sub_dir, csv_filename):
    start_time = datetime.now()

    create_json_files(sub_dir)
    json_data_list = read_all_json_files(sub_dir)

    df = pd.DataFrame(json_data_list)
    df.to_csv(csv_filename, index=False)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time.total_seconds():.2f} seconds")

if __name__ == "__main__":
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

    create_dataframe_and_csv(sub_dir, csv_filename)




