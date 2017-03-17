import pyautogui
import time

print('Start...')
time.sleep(2)

def automateGameCreate():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('l')
    pyautogui.keyUp('l')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

def isUrlChanged(url):
    if url != 'https://en.lichess.org/':
        return True
    else:
        return False

from tkinter import Tk
curURL = (Tk().clipboard_get())
print (isUrlChanged(curURL))



