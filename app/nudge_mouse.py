"""Nudges the mouse to prevent messaging programs from going into idle mode."""

import time
import pyautogui

def main():
    """Keeps the mouse active to prevent idle mode."""
    print('NudgeBot activated. Press CTRL-C to quit.')
    try:
        while True:
            # Move the mouse right and then back left
            pyautogui.moveRel(10, 0, duration=0.5)
            pyautogui.moveRel(-10, 0, duration=0.5)
            time.sleep(10)  # Wait for 10 seconds before the next nudge
    except KeyboardInterrupt:
        print('NudgeBot deactivated.')

if __name__ == "__main__":
    main()
