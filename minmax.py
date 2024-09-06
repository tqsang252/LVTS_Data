import csv

# Open the CSV file for reading
with open('2023_quy1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if it exists
    
    # Initialize min and max values
    min_val = float('inf')
    max_val = float('-inf')
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Assuming the data is in the first column of each row
        data = float(row[1])
        
        # Update min and max values
        min_val = min(min_val, data)
        max_val = max(max_val, data)

print("Minimum value:", min_val)
print("Maximum value:", max_val)