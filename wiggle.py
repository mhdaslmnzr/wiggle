import pyautogui
import threading
import datetime
import time
import random

# Disable PyAutoGUI fail-safe
pyautogui.FAILSAFE = False

# Function to display an intro graphic
def intro_graphic():
    print("""
    *****************************
    * Welcome to Mouse Clicker 3000 *
    *****************************
    """)

# Function to click the mouse
def clickMouse():
    pyautogui.click()
    print(f"Mouse clicked at {datetime.datetime.now()}")
    # Schedule the next click at a random interval between 5 to 10 seconds
    threading.Timer(random.uniform(5, 10), clickMouse).start()

# Main function to start the process
def main():
    intro_graphic()
    print("Starting Mouse Clicker 3000...")
    clickMouse()

# Start the main function
main()

# Keep the script running until manually stopped
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nMouse Clicker 3000 stopped by user.")
