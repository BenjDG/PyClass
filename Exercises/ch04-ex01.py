#!/usr/bin/env python3
my_set = set()
numbers_not_added = list()
while True:
    number = input("Enter a number or end: ")
    if number == 'end':
        break
    if (number in my_set):
        print("number is already in set")
        numbers_not_added.append(number)
    else:
        my_set.add(number)
        print("number added")
print("my_set is: ", my_set)
print("numbers not added to my set: ", numbers_not_added)

        
