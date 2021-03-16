import pyautogui
from time import sleep
import numpy as np 
import win32con
import win32process
import subprocess

print(pyautogui.size()) # Print screen size in pixels
print(pyautogui.position()) # Print current cursor position
#pyautogui.moveTo(1440/2-1,900/2-1)
#sleep(2)
#pyautogui.moveRel(200,-200,1,pyautogui.easeOutQuad)

EXE_NAME = 'C:\Windows\system32\mspaint.exe'
si = win32process.STARTUPINFO()
si.dwFlags = win32con.STARTF_USESHOWWINDOW
si.wShowWindow = win32con.SW_MAXIMIZE
h_proc, h_thr, pid, tid = win32process.CreateProcess(None, EXE_NAME, None, None, False, 0, None, None, si)
print(h_proc, h_thr, pid, tid)
#subprocess.Popen('C:\Windows\system32\mspaint.exe',close_fds = True)

sleep(2)
pyautogui.moveTo(626,95,0.25)
pyautogui.click()
pyautogui.moveTo(637,138,0.25)
pyautogui.click()

(sizex, sizey) = pyautogui.size()
qpoints = 4

for qpoints in range(4,9):
    for i in range(0,qpoints+1):
        pyautogui.dragTo(int(300+150*np.cos(2*np.pi*i/qpoints)), int(350+150*np.sin(2*np.pi*i/qpoints)))
    

pyautogui.moveTo(15,600)
pyautogui.dragTo(700,600,0.5)

pyautogui.moveTo(15,600)
for t in range (16,620,2):
    pyautogui.dragTo(t+33,int(600-np.exp(-t/150)*100*np.sin(2*np.pi*(t-16)/50)))

pyautogui.click(291,69)
pyautogui.click(600,300)
pyautogui.typewrite("Done with Python\nand pyautigui", interval = 0.1)
pyautogui.click(580,300)