import sys
import re
import argparse
import random
def main():
    print("\t\t\t\tAUTOHOTKEY-FISCGEN v.1.0(BETA)\n\t\t( P.S. : I'll add more features later if i feel like it :p )\n\n\t\t         _______________________________________________________________\n\t\tExample: |python3 fiscgen.py -i input.txt -o output.ahk -s 150,250 -k F4|\n\t\t         ---------------------------------------------------------------\n\n")
    print("\nA simple script to generate AutoHotkey scripts from simple paintext files, the resulting script is to be run using AutoHotkey and it types itself out .\n")
    print("Created by: HackerPrat")
    parser = argparse.ArgumentParser(description='\nAUTOHOTKEY-FILE-SCRIPT-GENERATOR\n')
    parser.add_argument('-i', '--input', help='\nName of the Input file', required=True)
    parser.add_argument('-o', '--output', help='\nName of the Output file', required=True)
    parser.add_argument('-s', '--speedrange', help='\nSet a type speed range\n Default: 150 to 250\n', required=False, default="150,250")
    parser.add_argument('-k', '--hotkey', help='\nHotkey to use for the script,\n Default: F4\n', required=False, default="F4")
    speedrange = parser.parse_args().speedrange
    speedrange = speedrange.split(",")
    speedrange = [int(i) for i in speedrange]
    hotkey = parser.parse_args().hotkey
    args = parser.parse_args()
    with open(args.input, 'r') as f:
        content = f.read()
    chars = re.split('', content)
    with open(args.output, 'w') as f:
        f.write(hotkey + "::\n") #you can change the 'F4' hotkey to another character after the script has been generated ;) .
        for char in chars:
            speed = random.randint(speedrange[0], speedrange[1])
            if char not in ['\n', '\t', ' ', '%', '`', ';']: #you can change the characters that are not properly typed out and even add more ;) .
                f.write('SendRaw, ' + char + "\nsleep "+ str(speed) +"\n")
            elif char == '%':
                f.write("SendRaw, `%\nsleep "+ str(speed) +"\n")
            elif char == '\n':
                f.write("SendInput, {ENTER}\nsleep "+ str(speed) +"\n")
            elif char == ' ':
                f.write("SendInput, {SPACE}\nsleep "+ str(speed) +"\n")
            elif char == ';':
                f.write("SendInput, {;}\nsleep "+ str(speed) +"\n")
            elif char == '`':
                f.write("SendRaw, ``\nsleep "+ str(speed) +"\n")
        f.write("return")
    with open(args.output, 'r') as f:
        lines = f.readlines()
    with open(args.output, 'w') as f:
        del lines[1]    #Don't even
        del lines[-3]   #think about
        del lines[-2]   #touching this
        for line in lines:
            f.write(line)
    print("\n\nOutput:\n\nIt's Done!\n\n\tGenerated Script: " + args.output + "\n\tThe Hotkey is : "+ hotkey +"\n\n\tYou can change the hotkey to something else by replacing the default 'F4' with another character but it's not recommended.\n\n Enjoy!\n")
if __name__ == '__main__':
    main()
    sys.exit(0)