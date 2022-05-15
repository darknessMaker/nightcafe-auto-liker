try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui
        
        
try:
    from time import sleep
except:
    os.system("pip install time")
    from time import sleep
        
        
try:
    import win32api, win32con
except:
    os.system("pip install pywin32")
    import win32api, win32con

        
confid=.975
failStreak=0

def click():
    win32api.SetCursorPos(position)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


##while True:
##    heart_location = pyautogui.locateOnScreen('heart.png', confidence=confid)
##    if heart_location==None:
##        confid-=.025
##    else:
##        break
while pyautogui.position()[0]>5 and pyautogui.position()[1]>5:
    heart_location = pyautogui.locateOnScreen('heart.png', confidence=confid, grayscale=True)
    if heart_location!=None:
        button_x, button_y=pyautogui.center(heart_location)
        position=button_x, button_y
        click()
        failStreak=0
    elif failStreak==10:
        heart_location = pyautogui.locateOnScreen('refresh button.png', confidence=confid, grayscale=True)
        button_x, button_y=pyautogui.center(heart_location)
        position=button_x, button_y
        click()
        win32api.SetCursorPos([pyautogui.position()[0], pyautogui.position()[1]+110])
        failStreak=0
    else:
        failStreak+=1
    heart_location = None
    pyautogui.scroll(-460)
    sleep(1)
    
exit()
