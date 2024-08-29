import sys
import csv

name = []

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name.append({"name": row['name'].split(', '), "house" : row['house']})

        with open(sys.argv[2], "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames = ["first", "last", "house"])
            writer.writeheader()
            for i in name:
                writer.writerow({"first":i['name'][1], "last": i['name'][0], "house": i['house']})


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")