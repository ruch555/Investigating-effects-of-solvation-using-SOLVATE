import os
import pandas as pd


def add_name_column_to_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter only CSV files
    csv_files = [f for f in files if f.endswith('.csv')]

    # Loop through each CSV file
    for csv_file in csv_files:
        csv_filename = os.path.join(folder_path, csv_file)
        file_name = os.path.splitext(csv_file)[0]  # Extract file name without extension

        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_filename)

        # Insert a new column named "Name" as the first column and fill it with the file name
        df.insert(0, 'Name', file_name)

        # Write the modified DataFrame back to CSV
        df.to_csv(csv_filename, index=False)


# Example usage:
folder_path = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters\categoricaltally"
add_name_column_to_folder(folder_path)
print("Name columns added to all CSV files in the folder successfully.")
