# Stack problem in python
# Created date: 16th March 2025 12:00pm

import sys


def ins(insVal):
    stack.append(insVal)


def pop():
    if not stack:
        print("Stack Underflow")
        return -1
    else:
        popVal = stack.pop()
        return popVal


def display():
    # print("stack is:", stack)
    for items in stack:
        print(items)


stack = []
while True:
    print("1. Insert")
    print("2. Remove")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        insVal = int(input("Enter insert value: "))
        ins(insVal)
    elif choice == 2:
        popVal = pop()
        print("Popped value: ", popVal)
    elif choice == 3:
        display()
    else:
        sys.exit()
