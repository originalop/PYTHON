file = open("Sample.txt", "r")
print(file.read(5))   # Reads first 10 characters
print(file.readline()) # Reads a single line
print(file.readlines()) # Reads all lines into a list
file.close()