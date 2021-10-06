#!/usr/bin/env python3

def mark():
    print("\nThis is mark() in mission_control.py")
    print("__name__ = " + __name__)

def main():
    print("This is mission_control.py.")
    print("__name__ = " + __name__)
    mark()

if __name__ == "__main__":
    main()
