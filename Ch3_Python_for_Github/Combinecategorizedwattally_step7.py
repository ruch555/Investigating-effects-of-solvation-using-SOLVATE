import os
import pandas as pd


def combine_csv_files(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Filter only CSV files
    csv_files = [f for f in files if f.endswith('.csv')]

    # Initialize an empty DataFrame to store the combined data
    combined_df = pd.DataFrame()

    # Read the first CSV file to initialize the combined DataFrame
    first_csv_file = os.path.join(folder_path, csv_files[0])
    combined_df = pd.read_csv(first_csv_file, index_col='Name')

    # Loop through each CSV file starting from the second one
    for csv_file in csv_files[1:]:
        csv_filename = os.path.join(folder_path, csv_file)
        file_name = os.path.splitext(csv_file)[0]  # Extract file name without extension

        # Read the CSV file into a DataFrame
        df = pd.read_csv(csv_filename, index_col='Name')

        # Update the combined DataFrame with values from the current DataFrame
        combined_df = combined_df.combine_first(df)

    # Fill missing values with 0
    combined_df.fillna(0, inplace=True)

    return combined_df


# Example usage:
folder_path = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters\categoricaltally"
combined_df = combine_csv_files(folder_path)
combined_df.to_csv(r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters\categoricaltally\otheranalysis\Combined.csv")
            # Save the combined DataFrame to a CSV file
