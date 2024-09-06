import pandas as pd
import csv , datetime

# open input CSV file as source 
# with open("master-data.csv", "r") as source: 
#     reader = csv.reader(source) 
    
#     with open("output.csv", "w", newline='', encoding='utf-8') as result: 
#         writer = csv.writer(result) 
#         for r in reader: 
#             try:
#                 writer.writerow((r[1], r[3]))
#             except:
#                 pass

def filter_and_sort_csv(file_path, year, output_file):
    current_datetime = datetime.datetime.now()
    # Đọc dữ liệu từ file CSV vào một DataFrame
    df = pd.read_csv(file_path, header=None)

    df.columns = ["Record_ID","Time","Temperature","Disolved Oxygen","Salinity","pH","Turbidity","DHT Temperature","DHT Moisture","Longitude","Latitude"]
    df['Time'] = pd.to_datetime(df['Time'],format="%d/%m/%Y %H:%M:%S", dayfirst=True)
     # Lọc dữ liệu theo năm được chỉ định
    filtered_data = df[df['Time'].dt.year == year]
    filtered_data.set_index('Time', inplace=True)
    filtered_data.index = pd.to_datetime(filtered_data.index)
    filtered_data.sort_index(inplace=True)
    filtered_data['Temperature'] = filtered_data["Temperature"].astype(float)
    filtered_data = filtered_data['Temperature']
    # df = df[df>=18]
    # current_datetime = current_datetime.replace(hour=current_datetime.hour, minute=0, second=0, microsecond=0)
    # df = df[df.index<pd.to_datetime(current_datetime, dayfirst=True)]
    # df = df.resample('H').mean()
    # df = df.dropna()
    filtered_data.to_csv(output_file, index=True,  header=None)
    print(f"Dữ liệu đã được ghi vào file: {output_file}")

# Đường dẫn đến file CSV
file_path = 'master-data.csv'
output_file = '2023.csv'
# Năm cần lọc
year_to_filter = 2023

# Lọc và sắp xếp dữ liệu
filtered_and_sorted_data = filter_and_sort_csv(file_path, year_to_filter, output_file)

# In ra dữ liệu đã lọc và sắp xếp
# print(filtered_and_sorted_data)