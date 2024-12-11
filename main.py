import os
import csv

def generate_output_file(output_path):
    """
    Generates a CSV file with sample data at the specified output path.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)  # Ensure the directory exists

    data = [
        ["Name", "Value"],
        ["Sample data", 123],
        ["Another row", 456]
    ]

    with open(output_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

    print(f"File generated at: {output_path}")

if __name__ == "__main__":
    # Define the output file path relative to the current workspace
    output_file = "results/output_data.csv"

    # Generate the file
    generate_output_file(output_file)

    print("Script completed successfully.")