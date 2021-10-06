#!/usr/bin/env python3

import os.path,sys
import mission_control
#from /home/student/mycode/main/mars/mars_base.py import mars_base
sys.path.append('/home/student/mycode/main/mars')
import mars_base
import michael

def main():
    print("This is moon_base.py.")
    print("__name__ = " + __name__)
    mission_control.main()
    mars_base.mars1()

if __name__ == "__main__":
    main()
