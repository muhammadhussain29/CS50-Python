import sys
from pyfiglet import Figlet

figlet = Figlet()
arr = figlet.getFonts()
inn = sys.argv

if(len(inn) == 2 or len(inn) >= 4):
    sys.exit("Invalid usage")

elif(len(inn) == 3):
    if((inn[1] != "-f" and inn[1] != "--font") or not(inn[2] in arr)):
        sys.exit("Invalid usage")
    else:
        figlet.setFont(font=inn[2])

f = input("Input: ")
print(figlet.renderText(f))
