#first crack at web page decoding
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)
for b in soup.find_all(class_="b"):
	if b.a:
		print(b.a.text.replace("\n", " ").strip())
	else:
		print(story_heading.contents[0].strip())