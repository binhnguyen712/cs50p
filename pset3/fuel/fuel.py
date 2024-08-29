def main():
    status = get_status()
    if status <= 1:
        print("E")
    elif status >= 99:
        print("F")
    else:
        print(f"{status}%")

def get_status():
    while True:
        try:
            f = input("Fraction: ").strip()
            n, d = f.split('/')
            if int(n) <= int(d):
                return round((int(n) / int(d)) * 100)
        except (ValueError, ZeroDivisionError):
            pass
main()