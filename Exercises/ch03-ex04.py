#!/usr/bin/env python3
lower = input("Input a lower limit number: ")
higher = input("Input a higher limit number: ")
step = input("Input a step value number: ")
result = ""
for i in range(int(lower), int(higher), int(step)):
    result += str(i) + " "
print(result)
