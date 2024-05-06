import pandas as pd
import json
import os

# Base file path without the page number and extension
base_file_path = 'page'
file_extension = '.csv'

# This will generate a list like: ['export-token-0xCfB24d3C3767364391340a2E6d99c64F1CBd7A3D_page1.csv', ...]
csv_files = [f"{base_file_path}{i}{file_extension}" for i in range(0, 8)]

# Combined data storage
combined_json_data = {}

# Process each file
for csv_file in csv_files:
    # Load the CSV data
    try:
        csv_data = pd.read_csv(csv_file)
    except FileNotFoundError:
        print(f"File {csv_file} does not exist. Skipping.")
        continue
    
    # Ensure 'Quantity' column is treated as a number and sum up quantities per 'From' address
    csv_data['Quantity'] = pd.to_numeric(csv_data['Quantity'], errors='coerce').fillna(0)
    aggregated_data = csv_data.groupby('From')['Quantity'].sum().to_dict()

    # Update the combined data with the new totals
    for address, quantity in aggregated_data.items():
        combined_json_data[address] = combined_json_data.get(address, 0) + quantity

# Calculate the grand total of all quantities
grand_total = sum(combined_json_data.values())

# Output the result to a JSON file
output_json_file = 'combined_output.json'
with open(output_json_file, 'w') as f:
    json.dump(combined_json_data, f, indent=4)

print(f"The combined JSON data has been saved to {output_json_file}.")
print(f"The grand total is: {grand_total}")
