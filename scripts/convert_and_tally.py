import pandas as pd
import json

# Load the CSV file
csv_file_path = '0422BSC.csv'  # Replace with your actual file path
csv_data = pd.read_csv(csv_file_path)

# Ensure 'Quantity' is a numeric type
csv_data['Quantity'] = pd.to_numeric(csv_data['Quantity'], errors='coerce').fillna(0)

# Group by 'From' address and sum quantities
aggregated_data = csv_data.groupby('From')['Quantity'].sum()

# Convert to JSON format
json_output = aggregated_data.to_dict()

# Calculate the grand total of all quantities
grand_total = sum(aggregated_data)

# Output the result to a JSON file
with open('output.json', 'w') as f:
    json.dump(json_output, f, indent=4)

print(f"The grand total is: {grand_total}")
