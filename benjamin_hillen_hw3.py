#To run this file, enter "python .\benjamin_hillen_hw3.py" in the command line in the directory with this file.
#
#ex. this file is stored in downloads, open command line in downloads, type "python ./benjamin_hillen_hw1.py" and press enter.
#
#Python must have interpreter in $PATH to run .py files.


import sys

year = input("Enter year: ")

#Report if year is a leap year or not
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")
