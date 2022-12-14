#! python3
# bullet point adder.py - Adds Wikipedia bullet point to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

#Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):    # Loops through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]  # Ass star to each string in "lines" list

text = '\n'.join(lines)

pyperclip.copy(text)

