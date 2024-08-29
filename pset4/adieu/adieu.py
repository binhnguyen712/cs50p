import inflect

p = inflect.engine()
l = []
try:
    while True:
        name = input("Name: ")
        l.append(name)
except EOFError:
    print()
    print("Adieu, adieu, to " + p.join(l))