import os

path = "C:\\Users\\srijayavel\\OneDrive\\Documents\\NFS Most Wanted"

if os.path.exists(path):
    print("the file exists")
    if os.path.isfile(path):
        print("that's a file")
    elif os.path.isdir(path):
        print("that's a directory")
else:
    print("the file does not exist")