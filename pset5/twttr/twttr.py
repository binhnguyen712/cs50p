def main():
    s = input("Input: ").strip()
    print("Output: ", shorten(s))

def shorten(word):
    vowels = ["a","e","u","i","o"]
    for c in word:
        if c.lower() in vowels:
            word = word.replace(c,"")
    return word

if __name__ == "__main__":
    main()