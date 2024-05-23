import json
import csv
import os

# Load the JSON file with claimed addresses
with open('claimed-addresses.json') as json_file:
    claimed_addresses = json.load(json_file)

# List of CSV files to search through (excluding page2.csv)
csv_files = [f'page{i}.csv' for i in range(5) if i != 2]

# Initialize a dictionary to store results
results = {}

# Loop through each CSV file
for csv_file in csv_files:
    # Check if the CSV file exists
    if os.path.exists(csv_file):
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                address = row['From']
                if address in claimed_addresses:
                    if address not in results:
                        results[address] = []
                    results[address].append({
                        'BlockNo': row['BlockNo'],
                        'Quantity': row['Quantity']
                    })
    else:
        print(f"File {csv_file} does not exist and will be skipped.")

# Print the results
for address, claims in results.items():
    print(f"Address: {address}")
    for claim in claims:
        print(f"  BlockNo: {claim['BlockNo']}, Quantity: {claim['Quantity']}")
