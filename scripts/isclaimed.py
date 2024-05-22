import csv
import time
from web3 import Web3
from web3.exceptions import ContractLogicError

# Replace with your Arbitrum RPC URL
arbitrum_rpc = "https://arbitrum.llamarpc.com"
web3 = Web3(Web3.HTTPProvider(arbitrum_rpc))

# Check connection
if not web3.is_connected():
    print("Failed to connect to the network")
    exit()
else:
    print("Connected:", web3.is_connected())

# Replace with your contract address and ABI
contract_address = '0x8e86de703e6145420580d383d3ed1befe0cd3221'
contract_abi = '''[
    {"inputs":[{"internalType":"address","name":"token_","type":"address"},{"internalType":"bytes32","name":"merkleRoot_","type":"bytes32"},{"internalType":"address","name":"treasury_","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},
    {"inputs":[],"name":"AlreadyClaimed","type":"error"},
    {"inputs":[],"name":"InvalidProof","type":"error"},
    {"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"index","type":"uint256"},{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Claimed","type":"event"},
    {"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},
    {"inputs":[{"internalType":"uint256","name":"index","type":"uint256"},{"internalType":"address","name":"account","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"bytes32[]","name":"merkleProof","type":"bytes32[]"}],"name":"claim","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"isClaimed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"merkleRoot","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[],"name":"token","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},
    {"inputs":[],"name":"treasury","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},
    {"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}
]'''

# Convert the contract address to a checksum address
checksum_address = web3.to_checksum_address(contract_address)

# Load the contract
contract = web3.eth.contract(address=checksum_address, abi=contract_abi)

# Function to get isClaimed status with retries
def get_is_claimed_status(index, retries=3, delay=2):
    for attempt in range(retries):
        try:
            is_claimed = contract.functions.isClaimed(index).call()
            return is_claimed
        except ContractLogicError as e:
            print(f"ContractLogicError on index {index}: {e}")
        except Exception as e:
            print(f"Error on index {index}: {e}")
        time.sleep(delay)
    return None

# Check the isClaimed status for indexes 0 to 49
results = []
for index in range(50):
    is_claimed = get_is_claimed_status(index)
    results.append({'index': index, 'is_claimed': is_claimed})
    time.sleep(1)  # Pause to avoid rate limiting

# Save the results to a CSV file
csv_file = 'is_claimed_results.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['index', 'is_claimed'])
    writer.writeheader()
    writer.writerows(results)

print(f"Results saved to {csv_file}")
