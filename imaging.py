import pyautogui
import time
location = pyautogui.locateOnScreen("test.png", confidence = 0.8)
if location:
    print("Found at:", location)
else:
   print("Image not found") 
print(pyautogui.size())
pyautogui.click(pyautogui.center(location))
ss = pyautogui.screenshot()  
ss.save("demo.png")