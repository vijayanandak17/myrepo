import pyautogui
import time
import subprocess

# Step 1: Open Google Chrome
subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
time.sleep(3)

# Step 2: Go to Gmail
pyautogui.hotkey('ctrl', 'l')  # Focus address bar
time.sleep(1)
pyautogui.write('https://mail.google.com', interval=0.05)
pyautogui.press('enter')
time.sleep(10)  # Wait for Gmail to load completely

# Step 3: Click "Compose"
# You may need to adjust these coordinates for your screen
compose_button = pyautogui.locateOnScreen('compose_button.png', confidence=0.9)
if compose_button:
    pyautogui.click(compose_button)
else:
    pyautogui.click(x=100, y=200)  # Approximate location, adjust if needed

time.sleep(3)

# Step 4: Fill in the "To" field
pyautogui.write('vijayanandak@hotmail.com')
pyautogui.press('tab')  # Move to subject
time.sleep(1)

# Step 5: Fill in the subject
pyautogui.write('Automated Email')
pyautogui.press('tab')  # Move to body
time.sleep(1)

# Step 6: Type the body
pyautogui.write('This is a test email sent using PyAutoGUI.', interval=0.05)
time.sleep(1)

# Step 7: Send the email (Ctrl + Enter)
pyautogui.hotkey('ctrl', 'enter')

print("Email sent!")
