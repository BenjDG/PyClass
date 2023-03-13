#!/usr/bin/env python3
my_list = [1, 2, 3, 34, 45, 35, 45, 34, 78, 99]

while True:
    user_number = input("Enter a number: ")
    if user_number == "end":
        break
    try:
        user_num = int(user_number)
        print(my_list[user_num])
    except ValueError as err:
        print("ValueError, please enter a whole integer")
    # except Exception as err:
    # print(err)
