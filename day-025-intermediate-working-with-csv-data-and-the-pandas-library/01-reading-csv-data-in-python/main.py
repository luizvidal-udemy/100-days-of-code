import os
import csv
import pandas

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, "weather_data.csv")

# data = []
# with open(FILE_PATH) as file:
#     data  = file.readlines()
# data = data[1:]
# data = list(map(lambda item: item.strip(), data))

# with open(FILE_PATH) as file:
#     data = csv.reader(file)
#     temperatures = []

#     for row in list(data)[1:]:
#         temperatures.append(int(row[1]))
        
#     print(temperatures)

data = pandas.read_csv(FILE_PATH)
print(data)
print(data["temp"])