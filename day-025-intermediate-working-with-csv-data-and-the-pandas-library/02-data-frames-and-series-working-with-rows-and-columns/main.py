import os
import pandas

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(CURRENT_DIR, "weather_data.csv")
CREATED_FILE_PATH = os.path.join(CURRENT_DIR, "data.csv")


data = pandas.read_csv(FILE_PATH)

data_dict = data.to_dict()

temp_list = data["temp"].to_list()

avarage_temp = sum(temp_list) / len(temp_list)

# print(data["temp"].mean())
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# Get the max temperature day
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
students_data = {
    "students": ["Amy", "James", "Angela"],
    "score": [76, 56, 65]
}


students_data_frame = pandas.DataFrame(students_data)

students_data_frame.to_csv(CREATED_FILE_PATH)
