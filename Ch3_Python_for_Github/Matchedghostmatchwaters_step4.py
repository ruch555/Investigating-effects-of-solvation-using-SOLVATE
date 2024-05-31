# !WORKS ON FOLDERS!
import os
import pandas as pd

def process_csv(input_csv_file, output_folder):
    # Read the CSV file into a DataFrame
    data = pd.read_csv(input_csv_file)

    # Filter rows where "Fate" column contains "Ghost Match" or "Matched"
    filtered_data = data[data['Fate'].isin(['Ghost Match', 'Matched'])]

    # Filter rows where "Distance.1" column values are less than 5.0
    filtered_data = filtered_data[filtered_data['Distance.1'] < 5.0]

    # Initialize a list to store classifications
    classifications = []

    # Iterate over filtered data
    for index, row in filtered_data.iterrows():
        # Initialize classification
        classification = None

        # Check "ProtHB" column value
        if row['ProtHB'] == True:
            # Extract the first 2 characters of the "ProtHB Atoms" column
            prot_hb_atoms = str(row['ProtHB Atoms']).strip()[:2]
            # Classify based on the first 2 characters
            if prot_hb_atoms.startswith("O ") or prot_hb_atoms.startswith("N "):
                classification = "Point of evolution based on HB backbone interaction to protein"
            else:
                classification = "Point of evolution based on HB sidechain interaction to protein"
            # Check the ligand atom
            classification = check_ligand_atom(classification, row['Closest Lig Atom'])
        # Check "ProtHF" column value
        if row['ProtHF'] == True:
            # Extract the residue from "ProtHF Atoms"
            prot_hf_residue = str(row['ProtHF Atoms']).strip()[4:7]
            # Classify based on residue
            if prot_hf_residue in ["TRP", "PHE", "TYR"]:
                classification = "Point of evolution based on HF aromatic interaction to protein"
            else:
                classification = "Point of evolution based on HF aliphatic interaction to protein"
            # Check the ligand atom
            classification = check_ligand_atom(classification, row['Closest Lig Atom'])


        # If both "ProtHB" and "ProtHF" are False
        if not row['ProtHB'] and not row['ProtHF']:
            classification = "Point of evolution based on water in bulk"
            # Check the ligand atom
            classification = check_ligand_atom(classification, row['Closest Lig Atom'])

        # Append the classification to the list
        classifications.append(classification)

    # Add the classifications to the DataFrame as a new column
    filtered_data['Evolution Point'] = classifications

    # Extract only the "Prot Water Number" and "Evolution Point" columns
    output_data = filtered_data[["Prot Water Number", "Evolution Point"]]

    # Define the output CSV file path
    output_csv_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_csv_file))[0] + ".csv")

    # Append the output data to the CSV file without writing the header
    output_data.to_csv(output_csv_file, mode='a', header=False, index=False)
def check_ligand_atom(classification, closest_lig_atom):
    # Strip leading and trailing whitespace and extract the first atom
    closest_lig_atom = str(closest_lig_atom).strip()[0]
    # Update classification based on ligand atom
    if closest_lig_atom in ["O", "N"]:
        if "Point of evolution based on HB backbone interaction to protein" in classification:
            classification += " and HB interaction to ligand"
        else:
            classification += " and HB interaction to ligand"
    else:
        if "Point of evolution based on HB backbone interaction to protein" in classification:
            classification += " and HF interaction to ligand"
        else:
            classification += " and HF interaction to ligand"
    return classification





# Input folder containing CSV files
input_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\csvfiles\splitentries"

# Output folder for saving processed CSV files
output_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters"

# Iterate over CSV files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        input_csv_file = os.path.join(input_folder, filename)
        process_csv(input_csv_file, output_folder)


