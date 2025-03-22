try:
    f = open("Sample.txt", "r")
    s = f.read()
    f.close()
    print(s)
except:
    print("can not perform operation on file")