def main():
    str = input()
    str = convert(str)
    print(str)

def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x
main()