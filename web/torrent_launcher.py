"""Checks for emailed Magnet links and begins downloading them."""

import time
import subprocess
import imapclient
import pyzmail
from email.mime.text import MIMEText

def magnet_check():
    """Checks Gmail for Magnet links from a verified address and returns them."""
    magnets = []
    try:
        with imapclient.IMAPClient('imap.gmail.com', ssl=True) as imap_obj:
            imap_obj.login(BOT_EMAIL, BOT_PASS)
            imap_obj.select_folder('INBOX')
            unique_ids = imap_obj.search(['FROM ' + VERIFIED_EMAIL])

            if unique_ids:
                for identifier in unique_ids:
                    raw_message = imap_obj.fetch([identifier], ['BODY[]'])
                    message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
                    text = message.text_part.get_payload().decode(message.text_part.charset)

                    if VERIFICATION_PASS in text:
                        html = message.html_part.get_payload().decode(message.html_part.charset)
                        magnets.append(html)

                imap_obj.delete_messages(unique_ids)
                imap_obj.expunge()
    except Exception as e:
        print(f"An error occurred: {e}")

    return magnets

def main():
    while True:
        magnet_links = magnet_check()
        for link in magnet_links:
            try:
                subprocess.Popen([TORRENT_CLIENT, link])
            except Exception as e:
                print(f"Failed to open torrent client for link {link}: {e}")

        time.sleep(60 * 15)  # Sleep for 15 minutes

if __name__ == "__main__":
    TORRENT_CLIENT = '/usr/share/applications/qbittorrent'  # Adjusted path to be more realistic
    BOT_EMAIL = 'R@bot.com'
    BOT_PASS = 'aasjhgf8970875/asfa#'
    VERIFIED_EMAIL = 'Allowed@Email.com'
    VERIFICATION_PASS = 'verify-this!'

    main()
