import json

total_supply_tokens = 80  # 10 million tokens
total_supply_smallest_unit = total_supply_tokens * 10**18

supply_data = {
    "total_supply": str(total_supply_smallest_unit)
}
output_file_path = './total_supply_2.json'

with open(output_file_path, 'w') as file:
    json.dump(supply_data, file, indent=4)

print(f"Total supply has been saved to {output_file_path}")
