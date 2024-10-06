import sys
from tabulate import tabulate

menu = []

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    try:
        name , extension = sys.argv[1].split(".")
        if(extension != "csv"):
            raise IndexError
    except IndexError:
        sys.exit("Not a CSV file")

with open(sys.argv[1]) as file:
    for row in file:
        row = row.rstrip().split(",")
        menu.append(row)

print(tabulate(menu,tablefmt="grid",headers="firstrow"))