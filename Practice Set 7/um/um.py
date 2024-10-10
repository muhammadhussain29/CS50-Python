import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    string = s.split(" ")
    for val in string:
        if re.search(r"^um{1}\W*$",val,re.IGNORECASE):
            counter+=1
    return counter

if __name__ == "__main__":
    main()