ex = input("Expression: ").strip()
x,y,z = ex.split(" ")
if y == "+":
    print(float(int(x) + int(z)))
elif y == "-":
    print(float(int(x) - int(z)))
elif y == "*":
    print(float(int(x) * int(z)))
elif y == "/":
    print(float(int(x) / int(z)))

