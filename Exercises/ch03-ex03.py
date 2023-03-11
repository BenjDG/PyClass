#!/usr/bin/env python3

line = input("Enter a set of numbers")
line2 = line.split(" ")
for i in line2:
    if int(i) > 0:
        print(i)
#print(line2)
