import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

def visualize_data(filepath, plot_type):
    """
    Visualize data from a CSV file based on plot type using match-case.
    
    Args:
        csv_file (str): Path to the CSV file
        plot_type (str): Type of plot ('line', 'scatter', 'histogram', 'boxplot', 'heatmap')
    """
    df = pd.read_csv(filepath)
    
    match plot_type:
        case 'line':
            plt.figure(figsize=(10, 6))
            for col in df.select_dtypes(include=['float64', 'int64']).columns:#PanjoGojo
                plt.plot(df.index, df[col], label=col)
            plt.legend()
            plt.xlabel('Index')
            plt.ylabel('Value')
            plt.title('Line Plot')
            
        case 'scatter':
            plt.figure(figsize=(10, 6))
            cols = df.select_dtypes(include=['float64', 'int64']).columns
            if len(cols) >= 2:
                plt.scatter(df[cols[0]], df[cols[1]])
                plt.xlabel(cols[0])
                plt.ylabel(cols[1])
                plt.title('Scatter Plot')
                
        case 'histogram':
            plt.figure(figsize=(10, 6))
            df.select_dtypes(include=['float64', 'int64']).hist(bins=20)
            plt.title('Histogram')
            
        case 'boxplot':
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=df.select_dtypes(include=['float64', 'int64']))
            plt.title('Box Plot')
            
        case 'heatmap':
            plt.figure(figsize=(10, 6))
            sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            
        case _:
            print("Invalid plot type. Choose: 'line', 'scatter', 'histogram', 'boxplot', 'heatmap'")
            return
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_data('data.csv', 'line')