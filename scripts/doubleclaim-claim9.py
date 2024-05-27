import json

# Load the JSON data from the files
with open('combined_output.json', 'r') as file:
    combined_output = json.load(file)

with open('double-claimed.json', 'r') as file:
    double_claimed = json.load(file)

# Check for duplicate keys
duplicate_keys = [key for key in double_claimed.keys() if key in combined_output.keys()]

# Alert if there are any duplicate keys
if duplicate_keys:
    print("Alert: The following keys are present in both files:")
    for key in duplicate_keys:
        print(f"Key: {key}, Value in combined_output: {combined_output[key]}, Value in double_claimed: {double_claimed[key]}")
else:
    print("No duplicate keys found.")

