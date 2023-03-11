#!/usr/bin/env python3

my_set = set()

while True:
    data = input("enter a line (q to quit) ")
    if data == 'q':
        break
    lineword = data.split()
    for x in lineword:
        my_set.add(x)
        
print(my_set)
    

        
