import pyautogui
import time

#mouse operations
pyautogui.click(100,100)
time.sleep(2)
#pyautogui.rightClick(100,100)
#time.sleep(3)
#x,y = pyautogui.position()
#print(f"X: {x}, Y: {y}")
#pyautogui.rightClick(x,y)
#pyautogui.doubleClick(x,y)
pyautogui.dragTo(800, 200, duration=0.5)
#pyautogui.scroll(200)

#time.sleep(2)
#pyautogui.click(911,327)
#time.sleep(1)
#pyautogui.typewrite("Welcome to Keyboard Opns")


#pyautogui.write("python rpademo.py")
#time.sleep(5)
#pyautogui.press("Enter")

#pyautogui.hotkey("ctrl","a")

#image operations
#location = pyautogui.locateOnScreen("test.png", confidence = 0.8)
#print (location)