import random


def main():
    level = get_level()
    i = 0
    score = 0
    try:
        while i < 10:
            rand_x = generate_integer(level)
            rand_y = generate_integer(level)
            a = 0
            while True:
                answer = int(input(f"{rand_x} + {rand_y} = "))
                if answer != rand_x + rand_y:
                    print("EEE")
                    a = a + 1
                else:
                    score = score + 1
                    break
                if a == 3:
                    print(f"{rand_x} + {rand_y} = {rand_x+rand_y}")
                    break
            i = i + 1
        print("Score: ", score)
    except EOFError:
        pass
        print()
    except ValueError:
        print("EEE")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except (EOFError, ValueError):
            pass

def generate_integer(level):
    start = 10**(level - 1)
    end = (10**level) - 1
    if level == 1:
        return random.randint(0,end)
    elif level not in [1,2,3]:
        raise ValueError
    else:
        return random.randint(start, end)

if __name__ == "__main__":
    main()