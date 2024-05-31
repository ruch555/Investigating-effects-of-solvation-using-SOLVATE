# !WORKS ON FOLDER!
import os
import csv

# Function to split rows with multiple values in the "ProtHB Atoms" and "ProtHF Atoms" columns
def split_rows(row):
    entries_hb = row['ProtHB Atoms'].split('|')
    entries_hf = row['ProtHF Atoms'].split('|')

    # Determine the maximum number of entries to iterate through both lists
    max_entries = max(len(entries_hb), len(entries_hf))

    for i in range(max_entries):
        new_row = row.copy()
        if i < len(entries_hb):
            new_row['ProtHB Atoms'] = entries_hb[i].strip()
        else:
            new_row['ProtHB Atoms'] = ''

        if i < len(entries_hf):
            new_row['ProtHF Atoms'] = entries_hf[i].strip()
        else:
            new_row['ProtHF Atoms'] = ''

        yield new_row

# Function to process a single CSV file
def process_csv(input_csv_file, output_folder):
    output_csv_file = os.path.join(output_folder, os.path.basename(input_csv_file))
    new_rows = []

    with open(input_csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Fate'] in ['Absolute Displacement', 'Contact Displaced Bulk', 'Contact Displaced HF', "Contact SWB", "Matched", "Ghost Match"]:
                new_rows.extend(split_rows(row))

    # Write new rows to the output CSV file
    fieldnames = reader.fieldnames

    with open(output_csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in new_rows:
            writer.writerow(row)

# Function to process all CSV files in a folder
def process_csv_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_csv_file = os.path.join(input_folder, filename)
            process_csv(input_csv_file, output_folder)

# Example usage:
input_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\csvfiles"  # Path to your input folder
# containing CSV files
output_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\csvfiles\splitentries"  # Path to your
# output folder for saving processed CSV files
process_csv_files(input_folder, output_folder)


