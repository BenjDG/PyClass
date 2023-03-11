#!/usr/bin/env python3
global f
f = 0
global s
s = 1
def fun():
    def fibonacci():
        next = f
        f,s = s, f + s
        return next
    return fibonacci

result = fun()

for i in range(10):
    print(result(), end = " ")
print()
