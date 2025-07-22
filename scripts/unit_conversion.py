import json
from decimal import Decimal

# Path to your input JSON file
input_file_path = './mintlayer_final_distro.json'
# Path to the output JSON file
output_file_path = './updated_input.json'

# Load the existing JSON data
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Convert the balances to wei (smallest unit, assuming 18 decimal places)
converted_data = {account: str(int(Decimal(balance) * Decimal('1e18'))) for account, balance in data.items()}

# Save the updated balances back to a new JSON file
with open(output_file_path, 'w') as file:
    json.dump(converted_data, file, indent=4)

print(f"Updated balances have been saved to {output_file_path}")
