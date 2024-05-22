const Web3 = require('web3');
const fs = require('fs');

// Connect to the Arbitrum network
const web3 = new Web3('https://arbitrum.llamarpc.com');

// Replace with your contract address
const contractAddress = '0x8e86de703e6145420580d383d3ed1befe0cd3221';

// Replace with your contract ABI
const contractABI = [
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
];

// Load the contract
const contract = new web3.eth.Contract(contractABI, contractAddress);

// Function to get isClaimed status
async function getIsClaimedStatus(index) {
    try {
        return await contract.methods.isClaimed(index).call();
    } catch (error) {
        console.error(`Error fetching isClaimed for index ${index}:`, error);
        return null;
    }
}

// Check the isClaimed status for indexes 0 to 49
async function checkIsClaimed() {
    const results = [];
    for (let index = 0; index < 50; index++) {
        const isClaimed = await getIsClaimedStatus(index);
        results.push({ index, is_claimed: isClaimed });
        await new Promise(resolve => setTimeout(resolve, 1000));  // Pause to avoid rate limiting
    }

    // Save the results to a CSV file
    const csvFile = 'is_claimed_results.csv';
    const csvContent = results.map(result => `${result.index},${result.is_claimed}`).join('\n');
    fs.writeFileSync(csvFile, 'index,is_claimed\n' + csvContent);
    console.log(`Results saved to ${csvFile}`);
}

checkIsClaimed();
