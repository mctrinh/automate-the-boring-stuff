"""A stopwatch program with enhanced output and clipboard functionality."""

import time
import pyperclip

def main():
    # Display the program's instructions.
    print('Press ENTER to start. Press ENTER again to record a lap time. Press Ctrl+C to quit.')

    input()  # Start the stopwatch
    print('Started.')
    start_time = time.time()
    last_time = start_time
    lap_num = 1

    try:
        while True:
            input()  # Wait for ENTER key press
            lap_time = round(time.time() - last_time, 2)
            total_time = round(time.time() - start_time, 2)

            lap = f'Lap #{lap_num:2d} {total_time:5.2f} ({lap_time:6.2f})'
            print(lap, end='\r')  # Overwrite the previous line

            pyperclip.copy(lap)  # Copy latest lap to clipboard

            lap_num += 1
            last_time = time.time()  # Reset last lap time

    except KeyboardInterrupt:
        # Handle the Ctrl+C exception
        print('\nDone.')

if __name__ == "__main__":
    main()
