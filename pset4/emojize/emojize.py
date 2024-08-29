import emoji
try:
    s = input("Input: ")
    print("Output: ", emoji.emojize(s, language='alias'))
except EOFError:
    pass