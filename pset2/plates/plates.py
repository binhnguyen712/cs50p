def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    punctuation = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~."
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        if s[int(len(s)/2)] == "0":
            return False
        for c in range(len(s[2:])):
            if s[c] in punctuation:
                return False
            if s[c].isdigit() and len(s[0:c]) < len(s):
                if s[int(s[c]) + 1].isalpha():
                    return False
        return True
    else:
        return False


main()