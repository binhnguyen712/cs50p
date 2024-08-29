# 24-hour time
def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    h, m = time.split(":")
    return float(int(h) + float(float(m) / 60))

if __name__ == "__main__":
    main()

# 12-hour time
#def main():
#    time = input("What time is it? ").strip()
#    t, f = time.split(" ")
#    t = convert(t)
#    if f == "a.m.":
#        if 7 <= t <= 8:
#            print("breakfast time")
#    elif f == "p.m.":
#        if 6 <= t <= 7:
#            print("dinner time")
#        elif 0 <= t <= 1:
#            print("lunch time")

#def convert(time):
#    h, m = time.split(":")
#    if h == "12":
#        h = "0"
#    return float(int(h) + float(float(m) / 60))

#if __name__ == "__main__":
#    main() */
