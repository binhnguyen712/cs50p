d = {}
try:
    while True:
        item = input()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
except EOFError:
    d = dict(sorted(d.items()))
    try:
        for k in d:
            print(f"{d[k]} {k.upper()}")
    except KeyError:
        pass
    pass