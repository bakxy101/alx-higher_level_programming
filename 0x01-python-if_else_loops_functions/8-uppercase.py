#!/usr/bin/python3
def uppercase(str):
    ascii = 0
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            ascii = ord(ch) - 32
        else:
            ascii = ord(ch)
        print("{:c}".format(ascii), end="")
    print()
