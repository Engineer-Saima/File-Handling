# 1- Creating the file in computer using write (w) mode
file = open("First.py", "w")
file.write("This file is created.")
file.close()

file = open("First.txt", "w")
file.write("This file is created.")
file.close()


# 2- Creating file in computer using with keyword
with open("file.txt", "w") as file:
    file.write("This is pyhon text file created using with keywords.")
    

# 3- Creating file in computer using OS module
import os

#Define specific path
file_path = "C:\\Users\\YourName\\Desktop\\new_file.txt"
with open("file_path", "w") as file:

    file.write("This file is created using OS Module")


# Append the data into the file
with open("file.txt", "a") as file:
    file.write("This is appended data in the file using append a mode") 
