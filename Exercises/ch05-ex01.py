#!/usr/bin/env python3
my_list = input("Enter numbers separated by spaces: ")
my_split = my_list.split(" ")

def my_function(bob):
    print("bob: ", bob)
    new_bob = []
    for i in bob:
        if int(i) > 0:
            new_bob.append(i)
    return print(new_bob)


my_function(my_split)
