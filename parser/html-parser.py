import urllib2
response = urllib2.urlopen(url)
html = response.read()
url = "https://devpost.com/software/search?page=1&query=has%3Aimage"

# print(urllib.request.urlopen(url).read())