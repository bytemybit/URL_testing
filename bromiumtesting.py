__author__ = 'mccoydo'
# Script for Carl to read a list of URL's from a file then open them in Internet Explorer.

import webbrowser
import time
import sys
import os
from itertools import *


def openBrowser(lines):
    for item in lines:
        ie = webbrowser.get(webbrowser.iexplore)  # Set Internet Explorer as ie
        if not "www" in item:
            item = 'http://' + item
        ie.open(item)  # Open browser with supplied url
    time.sleep(45)  # Wait 45 seconds for something to happen in the Browser
    os.system('taskkill /F /IM iexplore.exe')  # Kill all the browser windows


if __name__ == '__main__':

    n = 10  # Nubmer of browser windows to open at a time
    with open(sys.argv[1]) as f:
        while True:
            next_n_lines = list(islice(f, n))  # Using islice to manage large files
            if not next_n_lines:
                break
            openBrowser(next_n_lines)  # sending 10 lines from the input file into openBrowser
            time.sleep(5)  # sleep for 5 seconds before sending 10 more into openBrowser