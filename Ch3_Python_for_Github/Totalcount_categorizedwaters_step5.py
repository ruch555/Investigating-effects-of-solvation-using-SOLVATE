# !WORKS ON FOLDERS!
import os
import pandas as pd

def tally_categories_folder(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over files in the input folder
    for csv_filename in os.listdir(input_folder):
        if csv_filename.endswith(".csv"):
            # Construct input and output file paths
            input_file = os.path.join(input_folder, csv_filename)
            output_file = os.path.join(output_folder, f"{os.path.splitext(csv_filename)[0]}.csv")

            # Process the CSV file
            tally_categories(input_file, output_file)

def tally_categories(input_file, output_file):
    # Read the original CSV file without headers
    df = pd.read_csv(input_file, header=None)

    # Count occurrences of each category
    category_counts = df[1].value_counts()

    # Create a new DataFrame to store the counts
    tally_df = pd.DataFrame(category_counts.items(), columns=['Category', 'Count'])

    # Transpose the DataFrame so categories become column headers
    tally_df = tally_df.set_index('Category').T

    # Write the transposed DataFrame to a new CSV file
    tally_df.to_csv(output_file, index=False)

# Example usage:
input_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters"
                # Path to the input folder containing CSV files
output_folder = r"C:\Users\Ruchira J\Desktop\SOP\thesis\3DSim\python\categoricalwaters\categoricaltally"
                # Path to the output folder for saving the output CSV files
tally_categories_folder(input_folder, output_folder)
