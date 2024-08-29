menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
try:
    while True:
        item = input("Item: ").strip()
        try:
            for k in menu:
                if item.title() == k:
                    total += menu[k]
                    print("Total: ${:.2f}".format(total))
        except KeyError:
            break
except EOFError:
    pass
    print()