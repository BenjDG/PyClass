#!/usr/bin/env python3
my_list = input("Enter numbers separated by spaces: ")
#print("my_list: ", my_list)
my_split = my_list.split(" ")
#print("my_split: ", my_split)

def my_function(*bob, bob_num):
    new_bob = []
    #print("type: ", type(bob))
    for i in bob:
        for j in i:
            print("*bob: ", *bob)
            print("bob: ", bob)
            #print("i: ", i)
            #print("j: ", j)
            #print("type: ", type(i))
            #print("type: ", type(j))
            if int(j) > bob_num:
                new_bob.append(i)
    
    return len(new_bob)

result = my_function(my_split, bob_num = 2)
print("result: ", result)

