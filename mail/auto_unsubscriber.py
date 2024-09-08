"""Scans emails for unsubscribe links and opens them in a browser."""

import webbrowser
import imapclient
import pyzmail
import bs4
import getpass

def find_unsubscribe_links(email, password):
    """Returns a list of unsubscribe links from a Gmail inbox."""
    unsub_links = []
    imap_client = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_client.login(email, password)
    imap_client.select_folder('INBOX', readonly=True)
    message_ids = imap_client.search(['ALL'])

    for msg_id in message_ids:
        raw_message = imap_client.fetch([msg_id], ['BODY[]'])
        message = pyzmail.PyzMessage.factory(raw_message[msg_id][b'BODY[]'])
        html_content = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html_content, 'lxml')

        for link in soup.select('a'):
            href = link.get('href')
            if href and 'unsubscribe' in href.lower():
                unsub_links.append(href)

    imap_client.logout()

    return unsub_links

def main():
    email = input('Enter your email address: ')
    password = getpass.getpass('Enter your email password: ')  # Secure password input
    links = find_unsubscribe_links(email, password)

    if links:
        for link in links:
            print(f'Opening unsubscribe link: {link}')
            webbrowser.open(link)
        print('All unsubscribe links have been opened.')
    else:
        print('No unsubscribe links found.')

if __name__ == "__main__":
    main()
