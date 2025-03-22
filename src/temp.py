import os
import sys

while True:
    print("\n1. Get current directory")
    print("2. Change directory")
    print("3. List directory")
    print("4. Create directory")
    print("5. Remove file")
    print("6. Remove empty directory")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Current Directory:", os.getcwd())

        elif choice == 2:
            path = input("Enter path: ")
            if os.path.exists(path):
                os.chdir(path)
                print("Changed directory to:", os.getcwd())
            else:
                print("Error: Path does not exist!")

        elif choice == 3:
            path = input("Enter path: ")
            if os.path.exists(path):
                print("Files & Folders:", os.listdir(path))
            else:
                print("Error: Path does not exist!")

        elif choice == 4:
            folder_name = input("Enter folder name: ")
            path = input("Enter path: ")
            full_path = os.path.join(path, folder_name)
            if not os.path.exists(full_path):
                os.mkdir(full_path)
                print("Directory created:", full_path)
            else:
                print("Error: Directory already exists!")

        elif choice == 5:
            file_name = input("Enter file name: ")
            path = input("Enter path: ")
            full_path = os.path.join(path, file_name)
            if os.path.exists(full_path):
                os.remove(full_path)
                print("File removed:", full_path)
            else:
                print("Error: File not found!")

        elif choice == 6:
            folder_name = input("Enter folder name: ")
            path = input("Enter path: ")
            full_path = os.path.join(path, folder_name)
            if os.path.exists(full_path) and os.path.isdir(full_path):
                os.rmdir(full_path)
                print("Empty directory removed:", full_path)
            else:
                print("Error: Directory not found or not empty!")

        elif choice == 7:
            print("Exiting program...")
            sys.exit()

        else:
            print("Invalid choice! Please enter a number between 1-7.")

    except ValueError:
        print("Error: Please enter a valid number!")
    except Exception as e:
        print(f"An error occurred: {e}")
