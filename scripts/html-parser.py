url = 'https://devpost.com/software/search?page=1'
import urllib.request
with urllib.request.urlopen(url) as response:
  html = response.read()

soup = BeautifulSoup(html, 'html.parser')