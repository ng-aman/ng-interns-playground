import os 
import json
import datetime 
from tqdm import tqdm 
import time 
import argparse

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate JSON files with timestamp information.")
    parser.add_argument("--num_files", type=int, default=100000, 
                        help="Number of JSON files to generate (default: 100000)")
    return parser.parse_args()

# Get command-line arguments
args = parse_arguments()

# Get the number of CPU cores
num_cores = 8

# Storing the current directory path
curr_dir = os.getcwd()

# Joining the new directory into the current directory
sub_dir = os.path.join(curr_dir, "file_data")

if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)
    print("Created sub_directory to generate json files")

# tqdm is used to create a progress bar
current_datetime = datetime.datetime.now() 

# Use args.num_files instead of a hardcoded value
for i in tqdm(range(1, args.num_files + 1), desc="Generating Files", unit="file"):
    tic = time.time()
    file_name = f'json_file_{i}.json'
    json_file_path = os.path.join(sub_dir, file_name).replace(os.path.sep, '/')

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
