# CODE PART 1 - !WORKS ON FOLDER FOR PROTHB AND CLOSEST PROT ATOM!
# import os
# import pandas as pd
#
# def process_csv(input_csv_file, output_csv_file):
#     # Read the input CSV file
#     data = pd.read_csv(input_csv_file)
#
#     # Filter rows based on values in the "Fate" column
#     filtered_data = data[data['Fate'].isin(['Absolute Displacement', 'Contact Displaced Bulk', 'Contact Displaced HF'])]
#
#     # Initialize a list to store water numbers and their categories
#     water_info = []
#
#     # Iterate over filtered data
#     for index, row in filtered_data.iterrows():
#         # Check if "ProtHB" column value is True
#         if row['ProtHB'] == True:
#             # Extract the first character of "Closest Prot Atom" column value
#             closest_prot_atom = str(row['Closest Prot Atom']).strip()[0]
#             # Classify based on the first character
#             if closest_prot_atom in ["O", "N"]:
#                 classification = "Forms HB with protein and closest atom is HB in protein"
#             else:
#                 classification = "Forms HB with protein but closest atom is HF in protein"
#             water_info.append((row['Prot Water Number'], classification))
#
#     # Append water numbers and their categories to the existing CSV file without headers
#     with open(output_csv_file, 'a') as f:
#         for water_number, category in water_info:
#             f.write(f"{water_number},{category}\n")
#
# # Specify input and output folders
# input_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\csvfiles\splitentries"  # Folder containing input CSV files
# output_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters"  # Folder to store updated CSV files
#
# # Process each CSV file in the input folder
# for input_file in os.listdir(input_folder):
#     if input_file.endswith(".csv"):
#         # Construct the paths for input and output files
#         input_csv_file = os.path.join(input_folder, input_file)
#         output_csv_file = os.path.join(output_folder, input_file)
#
#         # Process the CSV file and update the corresponding output file
#         process_csv(input_csv_file, output_csv_file)




# CODE PART 2 - ! WORKS ON FOLDERS FOR CONTACT SWB AND CLOSEST LIG ATOM!
import os
import pandas as pd

def process_csv(input_csv_file, output_csv_file):
    # Read the input CSV file
    data = pd.read_csv(input_csv_file)

    # Filter rows based on values in the "Fate" column
    filtered_data = data[data['Fate'].isin(['Contact SWB'])]

    # Initialize a list to store water numbers and their categories
    water_info = []

    # Iterate over filtered data
    for index, row in filtered_data.iterrows():
        # Check if "ProtHB" column value is True
        if row['Fate'] == 'Contact SWB':
            # Extract the first character of "Closest Lig Atom" column value
            closest_lig_atom = str(row['Closest Lig Atom']).strip()[0]
            # Classify based on the first character
            if closest_lig_atom in ["O", "N"]:
                classification = "Contact SWB and closest atom in ligand is HB"
            else:
                classification = "Contact SWB but closest atom in ligand is HF"
            water_info.append((row['Prot Water Number'], classification))

    # Append water numbers and their categories to the existing CSV file without headers
    with open(output_csv_file, 'a') as f:
        for water_number, category in water_info:
            f.write(f"{water_number},{category}\n")

# Specify input and output folders
input_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\csvfiles\splitentries"  # Folder containing input CSV files
output_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters"  # Folder to store updated CSV files

# Process each CSV file in the input folder
for input_file in os.listdir(input_folder):
    if input_file.endswith(".csv"):
        # Construct the paths for input and output files
        input_csv_file = os.path.join(input_folder, input_file)
        output_csv_file = os.path.join(output_folder, input_file)

        # Process the CSV file and update the corresponding output file
        process_csv(input_csv_file, output_csv_file)


