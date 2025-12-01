import csv
from statistics import mode

def calculate_statistics(data, choice):
    """
    Calculate various statistical functions based on user choice.
    
    Args:
        data: List of numbers. But arrays bhi use kar sakte ho . 
        choice: Integer representing the statistical function
    """
    match choice:
        case 1:
            # Mean (Central Tendency) - Average of all values
            # Logic: Sum all values and divide by count
            return sum(data) / len(data)
        
        case 2:
            # Median (Central Tendency) - Middle value when sorted
            # Logic: Sort data, then find middle element(s)
            # If odd length, return middle value; if even, return average of two middle values
            sorted_data = sorted(data)
            n = len(sorted_data)
            return sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        
       
        case 3:
            # Mode (Central Tendency) - Most frequently occurring value
            # Logic: Use statistics.mode() to find the value with highest frequency
            return mode(data)
        
        case 4:
            # Standard Deviation (Deviation) - Measure of spread around mean
            # Logic: Calculate variance, then take square root for standard deviation
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            return variance ** 0.5
        
        case 5:
            # Variance (Deviation) - Average squared deviation from mean
            # Logic: For each value, subtract mean and square it, then average all squared differences
            mean = sum(data) / len(data)
            return sum((x - mean) ** 2 for x in data) / len(data)
        
        case 6:
            # Range (Deviation) - Difference between max and min values
            # Logic: Find maximum and minimum values, then compute their difference
            return max(data) - min(data)
        
        case 7:
            # Kurtosis (Shape) - Measure of tail heaviness in distribution
            # Logic: Calculate fourth moment, divide by variance squared, subtract 3 for excess kurtosis
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            fourth_moment = sum((x - mean) ** 4 for x in data) / len(data)
            return (fourth_moment / (variance ** 2)) - 3
        
        case 8:
            # Skewness (Shape) - Measure of asymmetry in distribution
            # Logic: Calculate third moment divided by variance^1.5
            # Positive skewness: tail on right, mean > median (right-skewed)
            # Negative skewness: tail on left, mean < median (left-skewed)
            # Zero skewness: symmetric distribution
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            third_moment = sum((x - mean) ** 3 for x in data) / len(data)
            skewness = third_moment / (variance ** 1.5)
            
            if skewness > 0:
                return f"Positive Skewness: {skewness:.4f} (right-skewed)"
            elif skewness < 0:
                return f"Negative Skewness: {skewness:.4f} (left-skewed)"
            else:
                return f"Symmetric: {skewness:.4f} (no skew)"
            
        case 9:
            # Quartiles and Interquartile Range (IQR) - Measure of data distribution
            # Logic: Sort data, then calculate Q1 (25th percentile), Q2 (median), Q3 (75th percentile)
            # IQR = Q3 - Q1, represents the middle 50% of data
            sorted_data = sorted(data)
            n = len(sorted_data)
            q1 = sorted_data[n // 4] if n % 4 != 0 else (sorted_data[n // 4 - 1] + sorted_data[n // 4]) / 2
            q2 = sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
            q3 = sorted_data[3 * n // 4] if n % 4 != 0 else (sorted_data[3 * n // 4 - 1] + sorted_data[3 * n // 4]) / 2
            iqr = q3 - q1
            return {"Q1": q1, "Q2 (Median)": q2, "Q3": q3, "IQR": iqr}
            # Median (Central Tendency) - Middle value when sorted
            # Logic: Sort data, then find middle element(s)
            # If odd length, return middle value; if even, return average of two middle values
            sorted_data = sorted(data)
            n = len(sorted_data)
            return sorted_data[n // 2] if n % 2 == 1 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
            
        
        case _:
            # Default case for invalid input
            # Logic: Return error message if choice doesn't match any case
            return "Invalid choice"


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


# Example usage
if __name__ == "__main__":
    # Read data from CSV file (update filepath as needed)
    filepath = "data.csv"
    data = read_csv_file(filepath, column_index=0)
    
    if data:
        print("1. Mean:", calculate_statistics(data, 1))
        print("2. Median:", calculate_statistics(data, 2))
        print("3. Mode:", calculate_statistics(data, 3))
        print("4. Standard Deviation:", calculate_statistics(data, 4))
        print("5. Variance:", calculate_statistics(data, 5))
        print("6. Range:", calculate_statistics(data, 6))
        