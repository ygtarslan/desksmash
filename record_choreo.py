import subprocess
import time
import sys

try:
    import pyautogui
except ImportError:
    print("Hold tight! Installing the required mouse library...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui", "pyobjc-core", "pyobjc"])
    import pyautogui

print("🤖 Director Mode: Engaging smooth robotic mouse control.")
print("Switch to your Desktop and start Screenize. Starting in 5 seconds...")

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# Feel free to adjust these X, Y coordinates to match your screen layout!
pyautogui.PAUSE = 0.5 

print("🎬 Action! Gliding to the DeskSmash Toolbar...")
# Move to the chainsaw/hammer icon (replace X, Y with your screen coordinates)
# tween makes it start slow, speed up, and slow down perfectly smoothly
pyautogui.moveTo(200, 300, duration=1.5, tween=pyautogui.easeInOutQuad)

print("Clicking tool...")
pyautogui.click()
time.sleep(0.5)

print("Gliding gracefully to the center of the desktop...")
pyautogui.moveTo(800, 600, duration=1.2, tween=pyautogui.easeInOutQuad)

print("Executing the chaotic sweep...")
# Simulates holding down the mouse and dragging across the screen
pyautogui.dragTo(1400, 650, duration=2.5, tween=pyautogui.easeInOutQuad, button='left')

print("Gliding to repair button...")
pyautogui.moveTo(200, 800, duration=1.5, tween=pyautogui.easeInOutQuad)
pyautogui.click()

print("✅ Cut! Perfect take.")
