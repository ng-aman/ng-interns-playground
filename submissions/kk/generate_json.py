
import json
from datetime import datetime
from pathlib import Path
from tqdm import tqdm
import multiprocessing

def generate_json_file(file_number, output_path, current_datetime):
    data = {
        "year": current_datetime.year,
        "month": current_datetime.month,
        "day": current_datetime.day,
        "current_datetime": current_datetime.strftime("%Y-%m-%d %H:%M:%S"),
        "file_number": file_number,
        "file_path": str(output_path / f"file_{file_number}.json")
    }

    with open(output_path / f"file_{file_number}.json", "w") as file:
        json.dump(data, file)

def generate_files_parallel(file_count, num_cores, output_path):
    output_path = Path(output_path)
    if not output_path.exists():
        output_path.mkdir(parents=True)

    current_datetime = datetime.now()

    with multiprocessing.Pool(num_cores) as pool, tqdm(total=file_count) as pbar:
        pool.starmap(generate_json_file, [(i, output_path, current_datetime) for i in range(1, file_count + 1)])
        pbar.update(file_count)

if __name__ == "__main__":
    file_count = 100000
    num_cores = multiprocessing.cpu_count()
    output_path = Path("output")

    generate_files_parallel(file_count, num_cores, output_path)

    print("Generation completed.")
