#write a python program to print the contents of a directory using the os module?

import os

# Specify the directory path
directory_path ='/new folder'

# List and print contents of the directory
contents = os.listdir(directory_path)

print("Contents of the directory:")
for item in contents:
    print(item)
