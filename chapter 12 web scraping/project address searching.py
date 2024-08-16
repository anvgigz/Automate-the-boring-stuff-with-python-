#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from the command line
    address = ' '.join(sys.argv[1:])
else:
    # Get address form clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)