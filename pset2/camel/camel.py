str = input("camelCase: ")
new = ""
for c in str:
    if c.isupper():
        c = "_" + c.lower()
    new += c
print("snake_case: ", new)
