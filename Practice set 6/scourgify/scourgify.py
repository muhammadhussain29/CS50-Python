import sys
import csv
from tabulate import tabulate

data = []

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            # read file and sperate first and last name
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row["name"].split(",")
                first = first.strip()
                data.append({"first":first,"last":last,"house":row["house"]})

    except FileNotFoundError:
        sys.exit("Could not read " + sys.argv[1])

with open(sys.argv[2],"w", newline="") as file:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
        writer.writerow(row)

