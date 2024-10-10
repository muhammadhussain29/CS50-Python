import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    part = r"\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b"
    if re.search(fr"^{part}\.{part}\.{part}\.{part}$",ip):
        return True
    else:
        False
    return False

if __name__ == "__main__":
    main()