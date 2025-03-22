import os

counter=1
for i in range(1,101, 1):
    os.rmdir(f"New Folder {counter}")