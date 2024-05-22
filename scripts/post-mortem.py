import json

# Load the claimed addresses from the JSON file
with open('claimed-addresses.json', 'r') as file:
    claimed_addresses = json.load(file)

# Calculate the total value
total_value = sum(claimed_addresses.values())

# Cut the total value in half
half_total_value = total_value / 2

# Print the results
print(f"Total value: {total_value}")
print(f"Half of the total value: {half_total_value}")
