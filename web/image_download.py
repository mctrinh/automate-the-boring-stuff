import requests
import os
import bs4

def download_xkcd_comics(start_url):
    # Create the directory for saving images
    os.makedirs('image_download', exist_ok=True)

    url = start_url
    while not url.endswith('#'):
        # Download the page
        print(f'Downloading page {url}...')
        try:
            res = requests.get(url)
            res.raise_for_status()
        except requests.RequestException as e:
            print(f'Error downloading page: {e}')
            break

        # Parse the page
        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Could not find comic image.')
        else:
            comic_url = 'http:' + comic_elem[0].get('src')
            # Download the image
            print(f'Downloading image {comic_url}...')
            try:
                img_res = requests.get(comic_url)
                img_res.raise_for_status()
            except requests.RequestException as e:
                print(f'Error downloading image: {e}')
                continue

            # Save the image to ./image_download
            image_path = os.path.join('image_download', os.path.basename(comic_url))
            with open(image_path, 'wb') as image_file:
                for chunk in img_res.iter_content(100000):
                    image_file.write(chunk)

        # Get the Prev button's URL
        prev_link_elem = soup.select('a[rel="prev"]')
        if not prev_link_elem:
            print('No more previous pages.')
            break
        
        prev_link = prev_link_elem[0]
        url = 'http://xkcd.com' + prev_link.get('href')

    print('Done.')

if __name__ == '__main__':
    download_xkcd_comics('http://xkcd.com')
