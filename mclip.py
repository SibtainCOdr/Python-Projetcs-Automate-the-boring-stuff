#! python3
# mclip.py - A multiclipboard-program
import sys, pyperclip

TEXT = {'agree': ''' Yes i agree. That sounds fine to me ''', 
        'busy': ''' Sorry, we can do this later this week or next week''',
        'upsell': ''' Would you consider making a monthly donation? '''}


if len(sys.argv) < 2:
    print('Usage: py mclip.py [keypharse] - copy phrase text')
    sys.exit() # Never forget the braces

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyphrase) 


