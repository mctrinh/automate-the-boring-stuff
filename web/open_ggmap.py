# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser
import sys
import pyperclip

def get_address():
    """Retrieve the address from command line arguments or clipboard."""
    if len(sys.argv) > 1:
        # Get the address from command line arguments.
        return ' '.join(sys.argv[1:])
    else:
        # Get the address from clipboard.
        return pyperclip.paste().strip()

def main():
    address = get_address()
    
    if not address:
        print("Error: No address provided. Please provide an address via command line or clipboard.")
        sys.exit(1)
    
    # Open the address in Google Maps
    maps_url = f'https://www.google.com/maps/place/{address}'
    webbrowser.open(maps_url)
    print(f'Opening map for address: {address}')

if __name__ == '__main__':
    main()
