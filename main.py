from fileholder import read_csv_file
from analytics import calculate_statistics

filepath = input("Enter CSV file path: ")
data = read_csv_file(filepath)

choice = int(input("Choose statistic: "))
result = calculate_statistics(data, choice)
print(result)


