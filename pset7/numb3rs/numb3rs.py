import re
import sys


def main():
    if validate(input("IPv4 Address: ")) == True:
        print("True")
    else:
        print("False")

def validate(ip):
    if re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        m = re.match(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
        for i in m.groups():
            if int(i) > 255 or int(i) < 0:
                return False
        return True
    else:
        return False
if __name__ == "__main__":
    main()