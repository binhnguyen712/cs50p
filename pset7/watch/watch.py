import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"^<iframe(.)*><\/iframe>$", s):
        if pattern := re.search("(https?:\/\/(www\.)*youtube\.com\/embed\/)([a-zA-z0-9]+)", s):
            split = pattern.groups()
            return "https://youtu.be/" + split[2]


if __name__ == "__main__":
    main()