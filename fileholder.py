import csv
import os

def read_csv_file(filepath, column_index=0):
    """
    Read numerical data from a CSV file and extract values from a specified column.
    """

    # Validate column index
    if column_index < 0:
        raise ValueError(f"column_index must be non-negative, got {column_index}")
    
    # Validate file extension
    if not filepath.lower().endswith('.csv'):
        raise ValueError("Invalid file format. Please upload a '.csv' file.")

    # Validate file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File '{filepath}' not found.")#PanjoGojo

    data = []

    try:
        # Open and read CSV file
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header row

            for row in reader:
                # Skip empty rows
                if not row:
                    continue

                # Column length check
                if column_index >= len(row):
                    raise ValueError(
                        f"CSV does not have column index {column_index}. "
                        f"Row only has {len(row)} columns."
                    )

                # Numeric conversion
                try:
                    value = float(row[column_index])
                except ValueError:
                    raise ValueError(
                        f"Non-numeric value found in column {column_index}: {row[column_index]}"
                    )

                data.append(value)

        return data

    except FileNotFoundError:
        raise
