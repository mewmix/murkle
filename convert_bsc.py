import pandas as pd
import json

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    data = pd.read_csv(csv_file_path)
    
    # Assuming you want to use the first two columns for the JSON key-value pairs
    # Convert those columns into a dictionary, removing commas from numeric strings
    data_dict = {row[0]: row[1].replace(',', '') if isinstance(row[1], str) and ',' in row[1] else row[1] 
                 for row in zip(data.iloc[:, 0], data.iloc[:, 1])}
    
    # Write the cleaned dictionary to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
        
    print(f"JSON file saved to {json_file_path}")

# Usage example:
csv_path = 'export-tokenholders-for-contract-0xCfB24d3C3767364391340a2E6d99c64F1CBd7A3D_BSC.csv'
json_path = 'output.json'
csv_to_json(csv_path, json_path)
