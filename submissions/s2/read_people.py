import json
import os
import pandas as pd

json_folder = os.path.join(os.getcwd(),"json_files")
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

                # Replace missing values with "MISSING"
        for key, value in data.items():
            if value is None or value == "":
                data[key] = "MISSING"

                # Append the data to the list
        all_data.append(data)
            
    except json.JSONDecodeError:
         print(f"Error: Invalid JSON format- {json_file_path}")
    except Exception as e:
                print(f"Error: {e} - {json_file_path}")

    # Create DataFrame
    df = pd.DataFrame(all_data)
    csv_output_path = os.path.join(os.getcwd(), "people_output.csv")


    # Save DataFrame to CSV
    df.to_csv(csv_output_path, index=False)

    print(f"Processing completed. Results saved to {csv_output_path}")



      
