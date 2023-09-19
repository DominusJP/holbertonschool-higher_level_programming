#!/usr/bin/python3
for i in range(0, 8):
    for a in range(1, 10):
        if i != a and i < a:
            print("{}{}, ".format(0, i), end='')
print("89")
