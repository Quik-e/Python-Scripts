# By Quik-e
# This bot will call the Italian Embassy in Argentina through WhatsApp Web for Windows until they respond. This will help get a meeting to get the Italian Passport.

import win32con
import win32process
import pyautogui
import time
import sys

def open_whatsapp():
    EXE_NAME = r'C:\Users\quiqu\AppData\Local\WhatsApp\WhatsApp.exe'
    si = win32process.STARTUPINFO()
    si.dwFlags = win32con.STARTF_USESHOWWINDOW
    si.wShowWindow = win32con.SW_MAXIMIZE
    h_proc, h_thr, pid, tid = win32process.CreateProcess(None, EXE_NAME, None, None, False, 0, None, None, si)
    connected = False
    while (connected == False):
        if (pyautogui.locateOnScreen("images/connected_dark.png") == None and pyautogui.locateOnScreen("images/connected_light.png") == None):
            print("Connecting to WhatsApp...")
        else:
            print("Connected")
            connected = True
    return

def vcall_contact(name = ""):
    pyautogui.hotkey("Ctrl","f") # This hotkey allows you to search for a conversation
    time.sleep(0.5)
    pyautogui.hotkey("Ctrl","a") # Selects all text in field. This is use to clear previous queries
    pyautogui.typewrite(name, interval = 0.1)
    pyautogui.click(132,250) # Position where the Conversation/Contact should be
    videoCallPos = None
    while(videoCallPos == None):
        videoCallPos = pyautogui.locateCenterOnScreen("images/videocall_dark.png")
        if videoCallPos == None: videoCallPos = pyautogui.locateCenterOnScreen("images/videocall_light.png")
        else: break
    pyautogui.click(videoCallPos,duration = 0.5)

def keep_vcalling():
    '''Keep calling on an open WhatsApp conversation'''
    videoCallPos = None
    while True:
        if(pyautogui.locateCenterOnScreen("images/end_call.png") == None):
            while(videoCallPos == None):
                videoCallPos = pyautogui.locateCenterOnScreen("images/videocall_dark.png")
                if videoCallPos == None: videoCallPos = pyautogui.locateCenterOnScreen("images/videocall_light.png")
                else: break
            pyautogui.click(videoCallPos,duration = 0.5)
            time.sleep(0.5)

if (__name__ == "__main__"):
    open_whatsapp()
    vcall_contact("Consolato Generale Italia Buenos Aires")
    keep_vcalling()