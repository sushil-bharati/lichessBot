import webbrowser
import pyautogui
import time
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "http://en.lichess.org"
webbrowser.open(url,new=new)
#import os
#os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe -ArgumentList @( '-incognito', 'www.en.lichess.org'" )
#mouse click

# def click(x,y):
#     win32api.SetCursorPos((x,y))
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
# click(10,10)
# print("Start...")
time.sleep(5)
pyautogui.moveTo(185,113) #hover to play button
pyautogui.click(185,132) #click Create a game
time.sleep(2) #wait for dialog box to appear
pyautogui.click(568,440) #click Casual - 568,440 and Rated - 712,440
pyautogui.click(565,576) #click black icon - 565,576, white icon - 716,586, random choice icon - 639,578

#
# x, y = pyautogui.position()
# positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
# print(positionStr)


