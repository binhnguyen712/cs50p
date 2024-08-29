month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    try:
        while True:
            date = input("Date: ").strip()
            if ',' in date and date[0].istitle():
                d1 = date.split(" ")
                d1[1] = d1[1].replace(',','')
                if 0 < int(d1[1]) <= 31:
                    print(f"{d1[2]}-{(month.index(d1[0]) + 1):02}-{int(d1[1]):02}")
                    break
            elif "/" in date:
                d2 = date.split("/")
                if d2[0].isnumeric() and 0 < int(d2[0]) <= 12 and 0 < int(d2[1]) <= 31:
                    print(f"{int(d2[2])}-{int(d2[0]):02}-{int(d2[1]):02}")
                    break
    except EOFError:
        pass
main()