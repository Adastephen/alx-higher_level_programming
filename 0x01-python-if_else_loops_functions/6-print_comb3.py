#!/usr/bin/python3
for i in range(0, 99):
    if i != 89:
        if ((i % 10 != 0) and ((i / 10) < (i % 10))):
            print("(0:02d)".format(i), end=', ')
    else:
        print("{}".format(i), end='')
