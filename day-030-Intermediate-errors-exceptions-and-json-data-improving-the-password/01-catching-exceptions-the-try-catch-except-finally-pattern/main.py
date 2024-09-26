# FileNotFound
# with open("inexistent_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)


# try: Something that might cause an exception

# except: Do this if there was an exception

# else: Do this if there was no exception

# finally: Do this no matter what happens

try:
    file = open("a_file.tx")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key_inexisting"])
    print(file.read())

except FileNotFoundError:
    file = open("a_file.txt", "w")

except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed.")
