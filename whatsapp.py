import pyautogui
import time

message = "😂 hlo kem chho  "  # Your prank message
count = 150  
# Number of times to send

time.sleep(5)  # Gives you 5 seconds to select the chat window

for i in range(count):
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(0.1 )  # Adjust speed as needed (0.1 seconds between messages)
