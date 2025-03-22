import os
import sys

while(True):
    print("1. Get current directory")
    print("2. Change directory")
    print("3. List directory")
    print("4. Create directory")
    print("5. Remove file")
    print("6. Remove empty directory")
    print("7. Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        print(os.getcwd())
    elif(choice==2):
        path=input("Enter path: ")
        print(os.chdir(path))
    elif(choice==3):
        path=input("Enter path: ")
        os.listdir(path)
    elif(choice==4):
        folder_name=input("Enter folder name: ") # Photos
        path=input("Enter path: ")
        os.mkdir(path+folder_name)
    elif(choice==5):
        file_name=input("Enter file name: ")
        path=input("Enter path: ")
        os.remove(path+file_name)
    elif(choice==6):
        folder_name=input("Enter folder name: ")
        path=input("Enter path: ")
        os.rmdir(path+folder_name)
    else:
        sys.exit()