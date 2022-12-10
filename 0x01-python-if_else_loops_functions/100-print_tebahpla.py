#!/usr/bin/python3
for i in range(ord('z'), ('a') - 1, - 1):
    if i % 2 != 0:
        c = 32
    else:
        c = 0
    print("{}".format(chr(i - c), end='')
