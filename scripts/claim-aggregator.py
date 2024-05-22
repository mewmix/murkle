import json
import csv
# JSON data
data = {
    "merkleRoot": "0xc8cb8444b00de3c2219f029bfe777c10708634f4f797c2d0cbd4e3aaa87a8492",
    "tokenTotal": "0x179c588c89d27368e8f0",
    "claims": {
        "0x03207642567238310Ba8EF2Cb7eBa0Ae8d2ABe84": {"index": 0, "amount": "0x1f04f6eceb1efd0000", "proof": ["..."]},
        "0x05e5d6C658D40bbE0857f5826081a5799b08DE32": {"index": 1, "amount": "0x022624087c85591c4800", "proof": ["..."]},
        "0x079e117238De1f75B00ad2bE5F181635a5206210": {"index": 2, "amount": "0x878678326eac900000", "proof": ["..."]},
        "0x1bB26A07ddb835Ff3A23ed584c68AF2629D8f2aE": {"index": 3, "amount": "0x7ca62bb47809bdb9e0", "proof": ["..."]},
        "0x2035F3Fb95080B4922964371133eBa1fE7D4CB2B": {"index": 4, "amount": "0x056bc75e2d63100000", "proof": ["..."]},
        "0x259F962e77262eE8d97cc6a112D0E0321323ea0d": {"index": 5, "amount": "0x01631382989cd8980000", "proof": ["..."]},
        "0x270A0De48967E60a419B872807A2A749D1E95fd2": {"index": 6, "amount": "0x1b2f704c53ca972640", "proof": ["..."]},
        "0x31110Fadb4401Fad566606905C03D9dAf3C87ce2": {"index": 7, "amount": "0x1a39a84be06eb90000", "proof": ["..."]},
        "0x3745A051dF3bA173a0b76Dc1af2491D18D3eD986": {"index": 8, "amount": "0x2870d46785c9680000", "proof": ["..."]},
        "0x388618D30Aa74b69956880032B2a8c8aAa7f6417": {"index": 9, "amount": "0x0db7148f8c6dd40000", "proof": ["..."]},
        "0x397E378287F2aAE2EabCAE5438d35AcBce8CD038": {"index": 10, "amount": "0x4108231ff94419a2c0", "proof": ["..."]},
        "0x39bbb8c321fdF88804C4f82487cb91115F1eC780": {"index": 11, "amount": "0x040e9dff48f8b88fc600", "proof": ["..."]},
        "0x3f73561DbeD168D1760920e6191Fa2AA2b563269": {"index": 12, "amount": "0x55a71ea47348fe6c00", "proof": ["..."]},
        "0x44051AD7FdA9Ae27bCB397AC753678D0753aE16D": {"index": 13, "amount": "0x15b3957200cded0000", "proof": ["..."]},
        "0x442bee95D7FeA5217431a02A0df4D10Bb1e85e68": {"index": 14, "amount": "0x0112c61a01ab2b5e8000", "proof": ["..."]},
        "0x4EEfB5A30eD2B43D4D84099f92A9b6Fac943B58f": {"index": 15, "amount": "0x0fed92554661460000", "proof": ["..."]},
        "0x4f941E5Da657375e75d6d92852431CC7bE3EF7A8": {"index": 16, "amount": "0x92d7a545c3f4d772c0", "proof": ["..."]},
        "0x5ACe64072c3B943d5901137543798Cf2C6871B09": {"index": 17, "amount": "0x1ae819e84729620000", "proof": ["..."]},
        "0x5a1870d746C45A8c66db40A6Faf3DbfdD0378EbB": {"index": 18, "amount": "0x3635c9adc5dea00000", "proof": ["..."]},
        "0x5e40F7f37338a21d087B6745d8F26fBD9b19F049": {"index": 19, "amount": "0x01267824b407d1e00000", "proof": ["..."]},
        "0x662deCcbc86b30D846E251cCde1A72C1f80483Cd": {"index": 20, "amount": "0x1db41e19e13a23b660", "proof": ["..."]},
        "0x6deE014F4164718f529feA368C0cC1d3798ceaE8": {"index": 21, "amount": "0x6cd7446a6e7e480000", "proof": ["..."]},
        "0x6e312cF46084F5Fc30b8E9c88c3D07408dd63020": {"index": 22, "amount": "0x2ef6d3377ad49705c0", "proof": ["..."]},
        "0x6e8231A42D9952238D1c7F8EBF8EB9e35d74867a": {"index": 23, "amount": "0x0579fb409c52d1a5c0", "proof": ["..."]},
        "0x716aa2eAd00881360f7Ea6876B91Ee629Fff5bA8": {"index": 24, "amount": "0x2b95bdcc39b6100000", "proof": ["..."]},
        "0x72590bDd8C9Cc95858854beB825F11376cdf0A7A": {"index": 25, "amount": "0x0ad78ebc5ac6200000", "proof": ["..."]},
        "0x76d7384B59F1a58c1CCe247d2E52751DCe4eEd21": {"index": 26, "amount": "0x03146e8bbe95e1400000", "proof": ["..."]},
        "0x7888A2D566B31d143D57e113Fd65305a83480C37": {"index": 27, "amount": "0x0d7f91b4bdd0440000", "proof": ["..."]},
        "0x795f0097a82C0F4A46b3e5Fd64E5d2aF1e148290": {"index": 28, "amount": "0xa2c96773b16edc2000", "proof": ["..."]},
        "0x7d1484181e6c382BC56E97a234987d78b9226d66": {"index": 29, "amount": "0x1043528d0984698000", "proof": ["..."]},
        "0x8277ba1481D2dFADb86d9002D123F81967215186": {"index": 30, "amount": "0x6db8a47c636ea00000", "proof": ["..."]},
        "0x8B9CE9E09283166d1056c4A8cd76362C642145BE": {"index": 31, "amount": "0x165c8113835bfb0000", "proof": ["..."]},
        "0x91011DD84fBD8a3e2c41505Cdc5c3fb359521c18": {"index": 32, "amount": "0x02b5e3af16b1880000", "proof": ["..."]},
        "0x943a445cF8128Ab27f7745B8ee6dFFAE6c9Fe61e": {"index": 33, "amount": "0x1b1ae4d6e2ef500000", "proof": ["..."]},
        "0x952b7237E985B673a587D58B0Aa2756f09c1B038": {"index": 34, "amount": "0x3a0f1c59994b5c0000", "proof": ["..."]},
        "0x99205da5A4664CdCD9995Db492297F95fc59d120": {"index": 35, "amount": "0x1043561a8829300000", "proof": ["..."]},
        "0xA782862589E5e353Bd450dF556354AdEe13B3388": {"index": 36, "amount": "0x0e4fbc69449f200000", "proof": ["..."]},
        "0xBa67cB850668EbDC213359e1ACdB96687717E200": {"index": 37, "amount": "0x9b3cf5e4cbae0f0000", "proof": ["..."]},
        "0xC81a77D1F0785ea0788DD4F6266C8C3Ae886dee3": {"index": 38, "amount": "0x0100f4b6d66757900000", "proof": ["..."]},
        "0xCc54DD4f4D079524A1C417bC2E2c2530179c6337": {"index": 39, "amount": "0x27bc6b206649540000", "proof": ["..."]},
        "0xD52deC06a8452A1B81306a84F585Dd2e25EcaF1b": {"index": 40, "amount": "0x29dc6d80b584a40000", "proof": ["..."]},
        "0xDEcBF5b0423e46cC1015d729D0574Da2C27feBe0": {"index": 41, "amount": "0x0dc38765054180a990", "proof": ["..."]},
        "0xE60E63Dae09bd69718AEE26F2603dc0B5d1E01Fa": {"index": 42, "amount": "0x2086ac351052600000", "proof": ["..."]},
        "0xF6193AB4d4bD0a2aC34B31dBe11a5b0017535a20": {"index": 43, "amount": "0x15af1d78b58c400000", "proof": ["..."]},
        "0xa10D89d792378e651e67899ad7600e9f7e3Eb429": {"index": 44, "amount": "0x56973e6e13193d4de0", "proof": ["..."]},
        "0xa3E7457240F0B624A5565D49f049de7eAcC40483": {"index": 45, "amount": "0x42d61038c34adb0000", "proof": ["..."]},
        "0xaB61914D7CEEf1090A5538D5C0098c64CbeC37B9": {"index": 46, "amount": "0x01d105e25ef5e0d80000", "proof": ["..."]},
        "0xb02268Fa64174635E5bC1c9a94A64B9Ef107293f": {"index": 47, "amount": "0x0420a79e97ce3e0000", "proof": ["..."]},
        "0xd42BEB9bc73D808F8C97211B225326Ea6D9f654B": {"index": 48, "amount": "0x1671677688b3b80000", "proof": ["..."]},
        "0xffDB6D24cc42455b11cF4aB9B688fb8b357D9fC5": {"index": 49, "amount": "0x1b1ae4d6e2ef500000", "proof": ["..."]}
    }
}

# List of is_claimed statuses
is_claimed_status = [
    True, False, False, False, False, False, True, False, True, True,
    True, True, False, True, False, False, True, True, True, True,
    False, False, False, True, False, True, True, False, True, False,
    True, False, False, False, True, False, False, True, True, True,
    False, False, False, True, True, True, False, False, True, True
]

# Creating the final list
results = []
for address, claim in data["claims"].items():
    index = claim["index"]
    is_claimed = is_claimed_status[index]
    results.append({"address": address, "index": index, "is_claimed": is_claimed})

# Printing the results
for result in results:
    print(result)


# Saving the results to a CSV file
csv_file = 'claimed_status_results.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['address', 'index', 'is_claimed'])
    writer.writeheader()
    writer.writerows(results)

print(f"Results saved to {csv_file}")