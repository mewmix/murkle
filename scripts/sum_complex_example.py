import json

# Load JSON data from a file
with open('complex_example.json', 'r') as file:
    json_data = json.load(file)

# Calculate the grand total
grand_total = sum(json_data.values())

print(f"The grand total is: {grand_total}")