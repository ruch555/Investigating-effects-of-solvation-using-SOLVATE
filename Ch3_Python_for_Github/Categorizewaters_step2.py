#!WORKS ON FOLDERS FOR SPLIT ENTRIES!
import os
import pandas as pd

def process_csv(csv_file, output_folder):
    # Read the CSV file
    data = pd.read_csv(csv_file)

    # Filter rows based on values in the "Fate" column
    filtered_data = data[data['Fate'].isin(['Absolute Displacement', 'Contact Displaced Bulk', 'Contact Displaced HF'])]

    # Initialize a dictionary to store values and their counts
    prot_wat_values = {}

    # Iterate over filtered data
    for index, row in filtered_data.iterrows():
        # Check if "ProtHB" is True
        if row['ProtHB']== True:
            # Extract the first 2 characters of the "ProtHB Atoms" column
            prot_hb_atoms = str(row['ProtHB Atoms']).strip()[:2]
            # Classify based on the first 2 characters
            if prot_hb_atoms.startswith("O ") or prot_hb_atoms.startswith("N "):
                classification = "HB to backbone of protein"
            else:
                classification = "HB to sidechain of protein"
            # Check the ligand atom
            classification = check_ligand_atom(classification, row['Closest Lig Atom'])
            # Update counts in the dictionary
            prot_wat_values[(row['Prot Water Number'], classification)] = prot_wat_values.get((row['Prot Water Number'], classification), 0) + 1

        # Check if "ProtHF" is True
        if row['ProtHF'] == True:
            # Extract the residue from "ProtHF Atoms"
            prot_hf_residue = str(row['ProtHF Atoms']).strip()[4:7]
            # Classify based on residue
            if prot_hf_residue in ["TRP", "PHE", "TYR"]:
                classification = "HF to aromatic residue of protein"
            else:
                classification = "HF to aliphatic residue of protein"
            # Check the ligand atom
            classification = check_ligand_atom(classification, row['Closest Lig Atom'])
            # Update counts in the dictionary
            prot_wat_values[(row['Prot Water Number'], classification)] = prot_wat_values.get((row['Prot Water Number'], classification), 0) + 1

        # If both "ProtHB" and "ProtHF" are False
        if not row['ProtHB'] and not row['ProtHF']:
            # Classify as "No interaction to protein"
            classification = "No interaction to protein"
            # Check the ligand atom
            classification = check_ligand_atom(classification, row['Closest Lig Atom'])
            # Update counts in the dictionary
            prot_wat_values[(row['Prot Water Number'], classification)] = prot_wat_values.get((row['Prot Water Number'], classification), 0) + 1

    # Now prot_wat_values contains the values you're interested in
    # Construct output file path dynamically based on input file name
    output_file = os.path.join(output_folder, os.path.basename(csv_file).replace(".csv", ".csv"))
    with open(output_file, 'w') as f:
        for (water_number, classification), count in prot_wat_values.items():
            for _ in range(count):
                f.write(f"{water_number},{classification}\n")

def check_ligand_atom(classification, closest_lig_atom):
    # Strip leading and trailing whitespace and extract the first atom
    closest_lig_atom = str(closest_lig_atom).strip()[0]
    # Update classification based on ligand atom
    if closest_lig_atom in ["O", "N"]:
        if "HB to backbone" in classification:
            classification += " displaced with HB by ligand"
        else:
            classification += " displaced with HB by ligand"
    else:
        if "HB to backbone" in classification:
            classification += " displaced with HF by ligand"
        else:
            classification += " displaced with HF by ligand"
    return classification

# Function to process all CSV files in a folder
def process_csv_files(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            input_csv_file = os.path.join(input_folder, filename)
            process_csv(input_csv_file, output_folder)

# Example usage:
input_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\csvfiles\splitentries"  # Path to your input folder containing CSV files
output_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters"  # Path to your output folder for saving processed CSV files
process_csv_files(input_folder, output_folder)
