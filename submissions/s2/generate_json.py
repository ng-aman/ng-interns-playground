import os 
import json
import datetime 
from tqdm import tqdm 
import time 


#storing current directory path
curr_dir = os.getcwd()
#joining new directory into current directory
sub_dir = os.path.join(curr_dir,"json_data")

# checking previous existence of same(new) directory 
if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)
    print("yo... successfully created sub_directory to generate json files")


current_datetime = datetime.datetime.now() 
for i in tqdm(range(1, 100001)):
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

        with open(json_file_path,"w") as files:
            files.write(json.dumps(json_file_data))


tac = time.time()
print(f"Time_taken to execute task {tac-tic}")
print("Relax..........your Task is complete")
