from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
l = figlet.getFonts()
if len(sys.argv) == 1:
    s = input("Input: ")
    try:
        figlet.setFont(font = random.choice(l))
    except IndexError:
        pass
    print("Output: ", figlet.renderText(s))

elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and sys.argv[2] in l:
        s = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print("Output: ", figlet.renderText(s))
    else:
        sys.exit("Invalid Useage")
else:
    sys.exit("INVALID USAGE")