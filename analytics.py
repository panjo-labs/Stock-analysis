from statistics import mode
from fileholder import read_csv_file
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
def calculate_statistics(data, choice):
    """
    Calculate various statistical functions based on user choice.
    
    Args:
        data: List of numbers or numpy array.
        choice: Integer representing the statistical function
    """
    data = np.array(data) #MADE BY PRANJAL SARASWAT AKA PanjoGojo
    match choice:
        case 1:
            return np.mean(data)
        case 2:
            return np.median(data)
        case 3:
            # Mode (Central Tendency) - Most frequently occurring value
            # Logic: Use statistics.mode() to find the value with highest frequency
            return mode(data)
        
        case 4:
            return np.std(data)
        case 5:
            return np.var(data)
        case 6:
            return np.ptp(data)
        case 7:
            return kurtosis(data) 
        #Ye bataata hai ki data ke tails kitne heavy ya light hain. Matlab
          #extreme values kitni baar aati hain
          #Agar tail zyada heavy → outliers zyada, peak sharp → leptokurtic, flat → platykurtic
        case 8:
            skewness = skew(data) #“Ye bataata hai ki data ka distribution left ya right ki taraf tilt hua hai
            if skewness > 0:
                return f"Positive Skewness: {skewness:.4f} (right-skewed)"#positive skew → tail right, negative skew → tail left.
            elif skewness < 0:
                return f"Negative Skewness: {skewness:.4f} (left-skewed)"
            else:
                return f"Symmetric: {skewness:.4f} (no skew)"
            
        case 9:
            q1, q2, q3 = np.percentile(data, [25, 50, 75])
            return {"Q1": q1, "Q2 (Median)": q2, "Q3": q3, "IQR": q3 - q1} #PanjoGojo
            
        case _:
            # Default case for invalid input
            # Logic: Return error message if choice doesn't match any case
            return "Invalid choice"
   
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
        
        print("7. Kurtosis:", calculate_statistics(data, 7))
        print("8. Skewness:", calculate_statistics(data, 8))
        print("9. Quartiles and IQR:", calculate_statistics(data, 9))