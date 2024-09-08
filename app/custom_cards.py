"""Create custom invitations from a guest list with flowery decorations."""

import os
from PIL import Image, ImageDraw, ImageFont

def create_card(name):
    """Creates a personalized invitation card with the provided name on it."""
    card = Image.new('RGBA', (360, 288), 'white')
    
    try:
        flower = Image.open('flower.png').convert('RGBA')
        card.paste(flower, (10, 40), flower)
    except FileNotFoundError:
        print("Error: 'flower.png' not found.")
        return

    draw_obj = ImageDraw.Draw(card)
    fonts_folder = '/usr/share/fonts/truetype'  # Adjusted path for better compatibility
    try:
        custom_font = ImageFont.truetype(os.path.join(fonts_folder, 'DejaVuSerif.ttf'), 72)
    except IOError:
        print("Error: Font file 'DejaVuSerif.ttf' not found.")
        return

    draw_obj.text((120, 100), name.strip(), fill='blue', font=custom_font)

    output_filename = '{}-invite.png'.format(name.strip())
    card.save(output_filename)
    print(f'Invitation saved as {output_filename}')

def main():
    """Reads the guest list and creates invitations."""
    try:
        with open('guests.txt') as f:
            guests = f.readlines()
    except FileNotFoundError:
        print("Error: 'guests.txt' not found.")
        return

    for guest in guests:
        create_card(guest)

    print('All invitations personalized and saved to the CWD - enjoy the dinner.')

if __name__ == "__main__":
    main()
