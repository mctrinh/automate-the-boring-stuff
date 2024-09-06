import requests
import sys
import webbrowser
import bs4

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py [search query]")
        sys.exit(1)

    print('Googling...')  # Display text while downloading the Google page

    # Construct the Google search URL
    search_query = ' '.join(sys.argv[1:])
    search_url = f'https://www.google.com/search?q={search_query}'

    # Fetch the search results page
    try:
        res = requests.get(search_url)
        res.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching search results: {e}")
        sys.exit(1)

    # Parse the search results page
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Retrieve top search result links
    link_elems = soup.select('.kCrYT a')  # Updated selector for links
    num_open = min(5, len(link_elems))

    # Open a browser tab for each result
    for i in range(num_open):
        href = link_elems[i].get('href')
        # The href attribute might include a Google-specific URL prefix
        full_url = f'https://www.google.com{href}'
        webbrowser.open(full_url)

    print('Done.')

if __name__ == '__main__':
    main()
