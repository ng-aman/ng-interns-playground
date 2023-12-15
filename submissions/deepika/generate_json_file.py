import os 
import json
import datetime 
from tqdm import tqdm 
import time 
import argparse

# Get the number of CPU cores
num_cores = 4

# Storing the current directory path
curr_dir = os.getcwd()

# Joining the new directory into the current directory
sub_dir = os.path.join(curr_dir, "file_data")

if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)
    print("Created sub_directory to generate json files")

# tqdm is used to create a progress bar
current_datetime = datetime.datetime.now() 

for i in tqdm(range(1, 100001), desc="Generating Files", unit="file"):
    tic = time.time()
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

tac = time.time()

print(f"Time taken to execute task: {tac - tic} seconds")
print(f"Task completed using {num_cores} CPU cores.")
