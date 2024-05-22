import csv
import json

# Load claim statuses from the CSV file
claimed_statuses = {}
with open('claimed_status_results.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        claimed_statuses[row['address']] = row['is_claimed'] == 'True'

# Load the existing data from complex_example.json
with open('complex_example.json', 'r') as file:
    data = json.load(file)

# Creating the final list of claimed and not claimed addresses with their respective values
claimed_addresses = {}
not_claimed_addresses = {}
for address, value in data.items():
    if address in claimed_statuses:
        if claimed_statuses[address]:
            claimed_addresses[address] = value
        else:
            not_claimed_addresses[address] = value

# Save the claimed addresses to a new JSON file
with open('claimed-addresses.json', 'w') as file:
    json.dump(claimed_addresses, file, indent=4)

# Save the not claimed addresses to a new JSON file
with open('notclaimed-addresses.json', 'w') as file:
    json.dump(not_claimed_addresses, file, indent=4)

print("Results saved to claimed-addresses.json and notclaimed-addresses.json")
