import os
import csv

def process_csv_files(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f'sorted_{filename}')

            with open(input_path, mode='r', newline='') as infile, open(output_path, mode='w', newline='') as outfile:
                reader = csv.DictReader(infile)
                writer = csv.DictWriter(outfile, fieldnames=['BlockNo', 'From', 'Quantity'])

                writer.writeheader()
                for row in reader:
                    quantity = row['Amount'].replace('"', '')  # Remove quotes if present
                    writer.writerow({'BlockNo': row['BlockNo'], 'From': row['From'], 'Quantity': quantity})

if __name__ == "__main__":
    input_directory = "."
    output_directory = "sorted"

    process_csv_files(input_directory, output_directory)
