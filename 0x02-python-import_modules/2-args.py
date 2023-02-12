#!/usr/bin/python3
if __name__ =="__main__":
    import sys
    count = len(sys.argv) -1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv))
    for i in range(len(sys.argv) -1):
        print("{}: {}".format(sys.argv[i + 1], i + 1))
