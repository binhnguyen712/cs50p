from datetime import date
import sys
import re
import inflect
def validate(dob):
    if re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", dob):
        y,m,d = dob.split("-")
        if date(int(y),int(m),int(d)):
            return date(int(y),int(m),int(d))
        else:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")

def main():
    p = inflect.engine()
    dob = validate(input("Date of Birth: "))
    today = date.today()
    diff = today - dob
    minutes = diff.days * 24 * 60
    words = p.number_to_words(minutes, andword = "")
    print(words.capitalize() + " minutes")

if __name__ == "__main__":
    main()