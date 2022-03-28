import time
import keyboard
import random
from pyautogui import *
import pyautogui
import win32api
import win32con


def yazma():
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')


while not keyboard.is_pressed("q"):
    a = pyautogui.pixel(994, 714)        #
    b = pyautogui.pixel(636,775)
    if a == (54, 57, 63):
        yazma()
        time.sleep(3.8)
    if a == (50, 53, 59):
        yazma()
        time.sleep(3.8)

    if a == (47, 49, 54):
        if b == (244,67,54):
            yazma()
            time.sleep(3.58)
        else:
            break
