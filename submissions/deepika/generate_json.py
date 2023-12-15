import json
import os
import multiprocessing
from datetime import datetime
from tqdm import tqdm
import argparse
import time 
def generate_json_file(file_number):
    current_time = datetime.now()
    metadata = {
        "year": current_time.year,
        "month": current_time.month,
        "day": current_time.day,
        "timestamp": current_time.strftime("%Y-%m-%d %H:%M:%S"),
        "file_name": f"file_{file_number}.json",
        "file_path": os.path.abspath(f"C:/Users/DELL/jsonproject/file_{file_number}.json")
    }

    with open(metadata["file_path"], 'w') as file:
        json.dump(metadata, file)

 # multiprocessing pool  to parallelize the execution of a function 
 # with is used as context manager

def generate_json_files(num_files, num_cores):
    with multiprocessing.Pool(processes=num_cores) as pool:
        list(tqdm(pool.imap(generate_json_file, range(1, num_files + 1)), total=num_files, desc="Generating Files"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate JSON files concurrently with multiprocessing.")
    parser.add_argument("num_files", type=int, help="Number of JSON files to generate")
    parser.add_argument("num_cores", type=int, help="Number of CPU cores to use")
    args = parser.parse_args()

    start_time = datetime.now()
    generate_json_files(args.num_files, args.num_cores)
    end_time = datetime.now()
    execution_time = end_time - start_time
    
    # generating timelaps between the files generation
    print("Execution was completed")
    print(f"\nOperation completed in {execution_time}.")
    time.sleep(3)


   
