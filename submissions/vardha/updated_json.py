
import json
import os
import pandas as pd

def process_json_files(json_folder):
    # list of JSON files in the folder
    json_files = [file for file in os.listdir(json_folder) if file.startswith("person_") and file.endswith(".json")]

    # Initialize an empty list to store data from all JSON files
    all_data = []

    # Loop through each JSON file
    for json_file in json_files:
        json_file_path = os.path.join(json_folder, json_file)
        try:
            # Read JSON file
            with open(json_file_path, 'r') as file:
                data = json.load(file)

            # Ensure the data is a dictionary
            assert isinstance(data, dict), f"Invalid JSON format in file - {json_file_path}"

            # Add entries for missing keys with values set to "MISSING"
            all_keys = set(key for person in all_data for key in person)
            missing_keys = all_keys.difference(data)
            for missing_key in missing_keys:
                data[missing_key] = "MISSING"

            # Replace missing values with "MISSING"
            for key, value in data.items():
                if value is None or value == "":
                    data[key] = "MISSING"

            # Append the data to the list
            all_data.append(data)

        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format - {json_file_path}")
        except Exception as e:
            print(f"Error: {e} - {json_file_path}")

    # Create DataFrame
    df = pd.DataFrame(all_data)

    # Save DataFrame to CSV
    csv_output_path = os.path.join(os.getcwd(), "people_output.csv")
    df.to_csv(csv_output_path, index=False)

    print(f"Processing completed. Results saved to {csv_output_path}")

# Example usage
json_folder_path = os.path.join(os.getcwd(), "json_files")
process_json_files(json_folder_path)