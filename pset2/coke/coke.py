amt = 50
while amt != 0:
    print("Amount Due: ", amt)
    insert = int(input("Insert Coin: "))
    if insert in (5,10,25):
        if(insert > amt):
            amt= insert - amt
            print("Change owed: ", amt)
            break
        elif(insert == amt):
            print("Changed owed: 0")
            break
        else:
            amt = amt - insert




