# File created by: Diego Avila

'''
create a program that helps me predict who will win the Premier League
and get relegated based on existing data
'''
# webbrowser opens a browser to a specific page
import webbrowser
webbrowser.open('https://automatetheboringstuff.com/2e/chapter12/')

#! python 3
# premmain.py - launches a table in the browser using data from the command line or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line
    address = ''.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyperclip.paste()


