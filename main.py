import threading
import time
import pyautogui
import keyboard
import winsound

from gui import StartMacroGUI, StopMacroGUI

running = False
StatusVar = "Press 'o' to stop..."


def StartMacro(key, interval, canvas, StatusLabel):
    global running

    if running:
        return
    
    try:
        interval = float(interval)
    except ValueError:
        print("Invalid argument (key)")
        return
    
    if not key:
        print("Invalid argument (key)")
        return
    
    running = True
    winsound.Beep(500, 500)

    Thread = threading.Thread(target=_macro_logic, args=(key, interval, canvas, StatusLabel))
    Thread.daemon = True
    Thread.start()

    StopThread = threading.Thread(target=_stop_on_key, args=(canvas, StatusLabel))
    StopThread.daemon = True
    StopThread.start()

def StopMacro():
    global running
    running = False


def _macro_logic(key, interval, canvas, StatusLabel):
    global running
    while running:
        canvas.itemconfig(StatusLabel, text=StatusVar)
        pyautogui.press(key)
        time.sleep(interval)

def _stop_on_key(canvas, StatusLabel):
    global running
    while running:
        if keyboard.is_pressed('o'):
            running = False
            canvas.itemconfig(StatusLabel, text="")
            winsound.Beep(500, 500)
            break
