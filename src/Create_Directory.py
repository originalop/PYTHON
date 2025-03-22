import os

counter=1
for i in range(1, 100, 1):
    os.mkdir(f"New Folder {counter}")
    counter+=1