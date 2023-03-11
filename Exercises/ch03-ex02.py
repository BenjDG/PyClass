#!/usr/bin/env python3

my_int1 = int(input("Integer 1?: "))
my_int2 = int(input("Integer 2?: "))
result = 0
for i in range(my_int1, my_int2 + 1):
    result += i
print(result)
