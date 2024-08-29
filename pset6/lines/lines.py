import sys


count = 0
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
else:
    try:
        if sys.argv[1].endswith(".py"):
            with open(sys.argv[1], "r") as file:
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip(" ") != "\n":
                        count = count + 1
            print(count)
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")