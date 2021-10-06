#!/usr/bin/env python3

def mars1():
    print("\nThis is mark() in mars_base.py")
    print("__name__ = " + __name__)

def main():
    print("This is mars_base.py.")
    print("__name__ = " + __name__)
    mars1()

if __name__ == "__main__":
    main()
