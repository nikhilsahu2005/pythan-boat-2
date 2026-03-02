import pyautogui
import pyperclip
import time

pyautogui.FAILSAFE = True

print("Screen size:", pyautogui.size())

time.sleep(5)  # Time to switch window

# Check current mouse position
print("Current mouse:", pyautogui.position())

# Drag slowly
pyautogui.moveTo(712, 190, duration=0.5)
pyautogui.dragTo(712, 1060, duration=1, button='left')

time.sleep(1)

pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.click(1506,254)

print("Copied:", pyperclip.paste())