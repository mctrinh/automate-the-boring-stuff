"""Sends out a message to a selected group of Google Hangouts contacts."""

import time
import pyautogui

def auto_message(name, message):
    """Searches for a friend on Google Hangouts and messages them."""
    print("Ensure the Google Hangouts 'Conversations' page is visible and "
          "your cursor is not currently on the page.")
    time.sleep(3)

    # Locate and click the search bar
    search_bar = pyautogui.locateOnScreen('search.png')
    if search_bar is None:
        print("Error: Search bar not found.")
        return
    
    pyautogui.click(search_bar)
    pyautogui.typewrite(name)
    time.sleep(1)

    # Locate and select the online friend
    online_select = pyautogui.locateOnScreen('online-friend.png')
    if online_select is None:
        print(f'Friend "{name}" not found or is currently offline.')
        return

    pyautogui.doubleClick(online_select)
    attempts = 3
    
    while attempts > 0:
        # Locate and click the message box
        message_box = pyautogui.locateOnScreen('message.png')
        if message_box is None:
            print("Error: Message box not found.")
            return

        pyautogui.click(message_box)
        pyautogui.typewrite(message)
        
        # Check if the message box is no longer present
        if pyautogui.locateOnScreen('message.png') is None:
            pyautogui.press('enter')
            pyautogui.press('esc')
            print(f'Message sent to {name}.')
            break
        else:
            if attempts == 1:
                print(f'Unable to send message to {name}.')
                pyautogui.press('esc')
            else:
                print(f'Sending message to {name} failed. {attempts - 1} attempts remaining.')
            attempts -= 1

def main():
    """Main function to get user input and send messages."""
    print('Enter the contacts you wish to send a message to (e.g., Bob, Bill):')
    send_to = input().split(',')
    
    print('Enter the message you wish to send out:')
    to_send = input()

    for contact in send_to:
        user = contact.strip()
        auto_message(user, to_send)

if __name__ == "__main__":
    main()
