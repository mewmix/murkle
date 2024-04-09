import json

# Total supply of tokens
total_supply_tokens = 10_000_000  # 10 million tokens
# Convert to smallest unit (assuming 18 decimal places, similar to Ethereum's wei)
total_supply_smallest_unit = total_supply_tokens * 10**18

# Example of how you might structure this in JSON format
# Assuming you want to just store the total supply value
supply_data = {
    "total_supply": str(total_supply_smallest_unit)
}

# Path to the output JSON file
output_file_path = './total_supply.json'

# Save the supply data to a JSON file
with open(output_file_path, 'w') as file:
    json.dump(supply_data, file, indent=4)

print(f"Total supply has been saved to {output_file_path}")
