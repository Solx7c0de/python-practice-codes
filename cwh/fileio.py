# # FOR READING A FILE
# f = open("rw.txt")
# data = f.read()
# print(data)
# f.close()


# # for writing to a file

# f = open("rw.txt","w")

# st = " this is the additiona statement"
# f.write(st)

# f.close()


# # READLINES FUNCTION

# f = open("rw.txt")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()

# readline func

f = open("rw.txt")

i=4

while (i >0):

    lines = f.readline()
    print(lines, type(lines))
    i-=1
f.close()



# TROUBLE SHOOTING IN CASE THE FILE TO BE ACCESSED ISNT IN THE WORKIUNG DIR:

# try:
#     with open("rw.txt", "r") as f:  # "r" is optional here as it's the default mode
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("The file 'rw.txt' does not exist.")

# import os

# file_path = "rw.txt"

# # Check if the file exists in the current directory
# if os.path.isfile(file_path):
#     print(f"File '{file_path}' exists.")
# else:
#     print(f"File '{file_path}' does not exist in the current directory '{os.getcwd()}'.")





