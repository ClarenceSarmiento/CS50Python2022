from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
command = ["-f", "--font"]

def convert_Figlet(font):
    text = input("Input: ")
    figlet.setFont(font=font)
    print("Output:")
    print(figlet.renderText(text))

def main():
    if len(sys.argv) < 2:
        rand_font = random.choice(figlet.getFonts())
        convert_Figlet(rand_font)
    elif len(sys.argv) > 2 and sys.argv[1] in command and sys.argv[2] in figlet.getFonts():
        convert_Figlet(sys.argv[2])
    else:
        sys.exit("Invalid usage")

main()