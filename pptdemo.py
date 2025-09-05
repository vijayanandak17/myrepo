import pyautogui
import time
import subprocess

myask = str(input("Enter PPT template type you want: "))

# Step 1: Launch PowerPoint
subprocess.Popen("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
time.sleep(2)  # Wait for PowerPoint to open

#click omn NEW
pyautogui.click(100,421)
time.sleep(2)
#click on Template search
pyautogui.click(335,487)
pyautogui.write(myask)
time.sleep(2)
# Step 2: Press Enter to open 'Blank Presentation'
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(1051, 370)
pyautogui.press('enter')

time.sleep(2)
pyautogui.click(1071, 328)
pyautogui.press('enter')
pyautogui.hotkey('Ctrl','a')
pyautogui.press('del')
pyautogui.write("Vijayanand A K")