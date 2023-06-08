# SimpleScraper - This program scrapes a website and displays it in clean text.
# This code was created with Google Bard on 2023-06-08 08:29:31 PST.

"""
Welcome to SimpleScraper!
"""

import requests

def render_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    text = text.replace('&lt;', '<').replace('&gt;', '>')
    text = text.strip()
    lines = text.split('\n')
    for line in lines:
        if line:
            print(line.rstrip())

if __name__ == "__main__":
    url = input("Enter the URL of the website: ")
    render_website(url)
