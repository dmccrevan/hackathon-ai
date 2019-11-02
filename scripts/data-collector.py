from bs4 import BeautifulSoup
import requests
import json

LINK_TO_SCRAPE = 'https://devpost.com/software/search?page='
LIMIT = 5511

def main():
    data = []
    for i in range(1, LIMIT+1):
        resp = requests.get(LINK_TO_SCRAPE+str(i))
        content = resp.content
        content = content.decode('utf-8')
        dic = json.loads(content)
        dic = dic['software']
        for item in dic:
            data.append((item['name'], item['tagline']))
    print(data)

if __name__ == "__main__":
    main()
