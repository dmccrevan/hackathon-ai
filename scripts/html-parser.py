import urllib.request
from bs4 import BeautifulSoup
import pickle
import threading

url = 'https://devpost.com/software/popular?page='
max_page = 5511
data = []


def worker(page_num):
    with urllib.request.urlopen(url + str(page_num)) as response:
        html = response.read()

    soup = BeautifulSoup(html, 'html.parser')
    entry_divs = soup.findAll("div", {"class": "software-entry-name"})

    for div in entry_divs:
        title = div.find('h5').contents[0].strip()
        tagline = div.findAll("p", {"class": "small tagline"})[0].contents[0].strip()
        data.append((title, tagline))

for page_num in range(max_page):
    t = threading.Thread(target=worker, args=(page_num,))
    print(f'looking at page {page_num} of {max_page}')
    t.start()

pickle.dump(data, open('data.pickle', 'wb'))

# pickle.load(open("data.pickle","rb"))
