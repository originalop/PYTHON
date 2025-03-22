try:
    file = open("Sample.txt", "r")  # Opens a file in read mode
    file.close()  # Closes the file
except:
    print("File doesn't exist!")
