import pyautogui
import time
import subprocess

# Step 1: Open Google Chrome
subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
time.sleep(3)  # Wait for browser to launch

# Step 2: Focus address bar
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)

# Step 3: Type the search query
pyautogui.write('latest cricket match score', interval=0.05)
time.sleep(1)

# Step 4: Press Enter
pyautogui.press('enter')

# VJ code
time.sleep(2)
#x,y = pyautogui.position()
#print(f"x:{x}, y: {y}")
pyautogui.click(654,621)
time.sleep(1)
pyautogui.scroll(500)
ss=pyautogui.screenshot()
ss.save("scores.png")
