#!/usr/bin/env python3

while True:
    try:
        number_1 = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
