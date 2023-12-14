import json
import os
import multiprocessing
from datetime import datetime
from tqdm import tqdm
import argparse
import time 
def create_json_file(file_number):
    now = datetime.now()
    metadata = {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
        "file_name": f"file_{file_number}.json",
        "file_path": os.path.abspath(f"C:/Users/MsK_PC/Desktop/data/file_{file_number}.json")
    }

    with open(metadata["file_path"], 'w') as file:
        json.dump(metadata, file)

 # `pool.imap` applies the `create_json_file` function to each value in the range concurrently.
 # `tqdm` is used to display a progress bar.

def generate_json_files(num_files, num_cores):
    with multiprocessing.Pool(processes=num_cores) as pool:
        list(tqdm(pool.imap(create_json_file, range(1, num_files + 1)), total=num_files, desc="Generating Files"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JSON files concurrently with multiprocessing.")
    parser.add_argument("num_files", type=int, help="Number of JSON files to generate")
    parser.add_argument("num_cores", type=int, help="Number of CPU cores to use")
    args = parser.parse_args()

    generate_json_files(args.num_files, args.num_cores)

    # generate a delay of 2s
    print("Execution completed")
    time.sleep(2)


   
