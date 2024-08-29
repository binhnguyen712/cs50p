import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(t):
    format = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",t)
    if format:
        split = format.groups()
        if int(split[1]) > 12 or int(split[5]) > 12:
            raise ValueError
        start = new_format(split[1], split[2], split[3])
        end = new_format(split[5], split[6], split[7])
        return start + " to " + end
    else:
        raise ValueError
def new_format(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time

if __name__ == "__main__":
    main()