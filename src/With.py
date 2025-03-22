with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # File is automatically closed after this block
