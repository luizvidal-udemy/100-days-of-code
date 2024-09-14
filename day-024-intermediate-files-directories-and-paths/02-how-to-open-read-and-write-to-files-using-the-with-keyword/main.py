path = "A:\\luiz-vidal\\github\\100-days-of-code\\day-024-intermediate-files-directories-and-paths\\02-how-to-open-read-and-write-to-files-using-the-with-keyword\\my_file.txt"

# file = open(path)
# contents = file.read()
# print(contents)
# file.close()

# Read file
# with open(path) as file:
#     contents = file.read()
#     print(contents)

# Write file
with open(path, mode="w") as file:
    file.write("Hello, my name is Luiz Vidal.\n")

