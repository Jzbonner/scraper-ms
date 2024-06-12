from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus" 
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
titles = soup.title.string
img = soup.find_all("img")

print(text, titles, img)