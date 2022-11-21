import time, sys

indent = 0 #how many spaces to indent
indentincresing = True # whether the indentation is increasing or not

try:
    while True:
        print(' '  * indent, end="")
        print('********')
        time.sleep(0.1) # paude of 1/10 of a second

        if indentincresing:
            indent = indent + 1
            if indent == 20:
                indentincresing = False

        else:
            indent = indent - 1
            if indent == 0:
                indentincresing = True

except KeyboardInterrupt:
    sys.exit
