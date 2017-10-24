#!/usr/bin/python3
import time 
import pyautogui
import numpy as np
def get_image(im):
    return im.crop((im.width/3,0,(2.151*im.width)/3,im.height))

def action(key):
    pyautogui.press(key)

time.sleep(5)
flag=0
n=int(input("Enter pages:\n"))

for i in range(n):
    time.sleep(0.4)
    im = pyautogui.screenshot()
    c=get_image(im)
    c.save(str(i)+".jpg")
    time.sleep(0.15)
    action("right")
