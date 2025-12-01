import csv
def read_csv_file(filepath, column_index=0):
    """
    Read numerical data from a CSV file.
    
    Args:
        filepath: Path to the CSV file. 
        column_index: Index of the column to extract (default: 0 for first column)
    
    Returns:
        List of numeric values from the specified column
    """
    data = []
    try:
        # Open and read CSV file
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            # Skip header row if needed
            next(reader, None)
            # Extract numeric values from specified column
            for row in reader:
                if row and len(row) > column_index:
                    data.append(float(row[column_index]))
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except ValueError:
        print("Error: Non-numeric value found in data.")
        return []