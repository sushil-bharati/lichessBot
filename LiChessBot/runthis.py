import chess
import chess.uci

import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import webbrowser
import pyautogui
import time
from tkinter import Tk

storage = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

def autoMove(cord):
    X1 = 868 - 65 * (storage[cord[0]]-1)
    Y1 = 180 + 65 * (int(cord[1])-1)
    X2 = 868 - 65 * (storage[cord[2]]-1)
    Y2 = 180 + 65 * (int(cord[3])-1)
    print("Clicking {0} {1} to {2} {3}".format(X1,Y1,X2,Y2))
    pyautogui.click(X1,Y1)
    pyautogui.click(X2,Y2)

def copyUrl():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('l')
    pyautogui.keyUp('l')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')


def isUrlSame(url):
    if url != 'https://en.lichess.org/':
        return False
    else:
        return True


def getMove(move, color, url):
    while True:
        response = urlopen(url).read()
        soup = BeautifulSoup(response, 'html.parser')
        tags1 = soup.findAll("div", class_="pgn")
        searchString = str(tags1)
        queryString = ''
        queryString = str(
            move) + "[.].([a-zA-Z]{1,2})(.{0,1})([a-zA-Z]{0,2})(.{0,1})([O]{0,1})([0-9]{0,1})"  # ([a-zA-Z]{1,2})(.{0,1})([a-zA-Z]{0,2})([0-9]{1})
        query = re.search(queryString, searchString)
        if query is not None:
            break
    found = str(query.group())
    store = found.split(' ')
    if color is 'black':
        return store[2]
    else:
        return store[1]

def autoGameCreate():
    pyautogui.moveTo(185,113) #hover to play button
    pyautogui.click(185,132) #click Create a game
    time.sleep(2) #wait for dialog box to appear
    pyautogui.click(712,440) #click Casual - 568,440 and Rated - 712,440
    pyautogui.click(565,576) #click black icon - 565,576, white icon - 716,586, random choice icon - 639,578

addr = "stockfish-8-win\\stockfish-8-win\\Windows\\stockfish_8_x64"  # load stockfish
engine = chess.uci.popen_engine(addr)  # start chess engine with stockfish
engine.uci()

board = chess.Board()  # initialize the board

#open the web in browser
url = "http://en.lichess.org"
webbrowser.open(url,new=2)

time.sleep(5) #wait time for browser to connect to the site

autoGameCreate() #set up game

flag2 = True
while flag2:
    copyUrl() #copy current url from browser
    dispUrl = (Tk().clipboard_get()) #get the url string from the clipboard
    flag2 = isUrlSame(dispUrl) #set flag False when url changes

cnt = 1
flag = True


print('Game Started in Window!!')
while flag:
    bate = getMove(cnt, 'white', dispUrl)  # what did white play on the board
    print(cnt, bate)
    board.push_san(bate)  # simulate
    engine.position(board)  # update the board
    move = engine.go(movetime=300)  # engine thinking... get the best move for black
    movedStr = str(move[0])  # best move found!
    nextMove = chess.Move.from_uci(movedStr)  # get the move to be fed into the board
    print(cnt, '...', board.san(nextMove), '(', nextMove, ')')
    autoMove(str(nextMove))
    board.push(nextMove)  # update the board with new move thought by PC
    cnt += 1
    # print (board)
    # print()
    # print()
    if board.is_stalemate():
        print("Stalemate")
        flag = False
    elif board.is_insufficient_material():
        print("Insufficient Material")
        flag = False
    elif board.is_game_over():
        print("Game over")
        flag = False
