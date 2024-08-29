import sys
import csv
from tabulate import tabulate
headers = []
table = []
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) >2:
    sys.exit("Too many command-line arguments")
else:
    try:
        if sys.argv[1].endswith(".csv"):
            with open(sys.argv[1], "r") as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                for row in reader:
                    table.append([row[headers[0]], row[headers[1]], row[headers[2]]])
            print(tabulate(table, headers, tablefmt = "grid"))

        else:
            sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")