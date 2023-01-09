#!/usr/bin/python3

def fizzbuzz():
    for num in range(1, 101):
        output = ""
        if num % 3 == 0:
            output += "Fizz"
        if num % 5 == 0:
            output += "Buzz"
        if (num % 3) != 0 and (num % 5) != 0:
            output = str(num)
        print(output, end=" ")
