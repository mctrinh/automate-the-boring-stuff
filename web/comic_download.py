"""Downloads any comic_download that have been updated since the last run."""

import os
import datetime
import requests
import bs4

def download_image(comic_url, save_path):
    """Download and save the comic image."""
    try:
        print(f'Downloading image {comic_url}')
        res = requests.get(comic_url)
        res.raise_for_status()
        with open(save_path, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
    except requests.exceptions.RequestException as e:
        print(f'Error downloading image: {e}')

def check_xkcd(last_url):
    """Download all XKCD comics released after the given URL."""
    base_url = 'https://xkcd.com'
    latest_url = base_url

    while True:
        res = requests.get(latest_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        comic_elem = soup.select('#comic img')
        if comic_elem:
            comic_url = 'https:' + comic_elem[0].get('src')
            filename = os.path.basename(comic_url)
            save_path = os.path.join('comic_download', filename)
            download_image(comic_url, save_path)

        prev_link = soup.select('a[rel="prev"]')
        if not prev_link or latest_url == last_url:
            break

        latest_url = base_url + prev_link[0].get('href')

    return latest_url

def check_smbc(last_url):
    """Download all SMBC comics released after the given URL."""
    base_url = 'https://www.smbc-comics.com/'
    res = requests.get(base_url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    home_url = soup.select('input[value]')[0].get('value')
    latest_url = 'https://www.' + home_url[7:]

    while True:
        res = requests.get(latest_url)
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'lxml')

        comic_elem = soup.select('#cc-comic img')
        if comic_elem:
            comic_url = 'https://www.smbc-comics.com/' + comic_elem[0].get('src')
            filename = os.path.basename(comic_url)
            save_path = os.path.join('comic_download', filename)
            download_image(comic_url, save_path)

        prev_link = soup.select('a[rel="prev"]')
        if not prev_link or latest_url == last_url:
            break

        latest_url = base_url + prev_link[0].get('href')

    return latest_url

def main():
    os.makedirs('comic_download', exist_ok=True)

    # Read last downloaded URLs
    try:
        with open('comic_download/last_downloaded.txt') as f:
            info = f.read().splitlines()
            date = info[0]
            last_xkcd = info[1]
            last_smbc = info[2]
    except FileNotFoundError:
        date = last_xkcd = last_smbc = ''
    
    date = datetime.datetime.now().strftime('%H:%M:%S on %d/%m/%Y')
    print(f'Last comic check = {date}')

    # Run functions and update file with new URLs
    xkcd_url = check_xkcd(last_xkcd)
    smbc_url = check_smbc(last_smbc)

    with open('comic_download/last_downloaded.txt', 'w') as f:
        f.write(f'{date}\n{xkcd_url}\n{smbc_url}')

    print('Finished.')

if __name__ == "__main__":
    main()
