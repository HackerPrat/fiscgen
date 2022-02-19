# fiscgen : AUTOHOTKEY-`FI`LE-`SC`RIPT-`GEN`ERATOR
*PS: ONLY USE PLAINTEXT FILES WITH THIS TOOL*

An [Autohotkey](https://www.autohotkey.com/) script generator written in python that takes plaintext files as input and outputs a `.ahk` script which types the entire content of the file out in a realistic enough way .

The wait periods before and after every keypress are randomly generated within a range supplied by the user . do `python3 fiscgen.py -h` for more info.

                         _______________________________________________________________
                Example: |python3 fiscgen.py -i input.txt -o output.ahk -s 150,250 -k F4|
                         ---------------------------------------------------------------
