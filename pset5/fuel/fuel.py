def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            if isinstance(percentage, int):
                print(gauge(percentage))
                break
        except ZeroDivisionError:
            raise ZeroDivisionError
        except ValueError:
            raise ValueError

def convert(fraction):

    try:
        x, y = fraction.split("/")
        if not x.isnumeric() or not y.isnumeric():
            raise ValueError
        else:
            if int(x) > int(y):
                raise ValueError
            elif int(y) == 0:
                raise ZeroDivisionError
            else:
                return round((int(x) / int(y))*100)
    except ValueError:
        raise ValueError



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()