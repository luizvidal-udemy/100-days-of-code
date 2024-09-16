import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)


student_data_frame = pandas.DataFrame(student_dict)

#Looping through a data frame:

# for (key, value) in student_data_frame.items():
#     print(value) # Not very useful

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)