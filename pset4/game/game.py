import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass
while True:
    try:
        rand = random.randint(1, level)
        guess = int(input("Guess: "))
        if guess < rand:
            print("Too small!")
        elif guess > rand:
            print("Too large!")
        else:
            print("Just right!")
            break
    except (EOFError, ValueError):
        pass
