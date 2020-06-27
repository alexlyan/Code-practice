

import requests
from bs4 import BeautifulSoup

#Request URL
page = requests.get("https://www.fifa.com/worldcup/players.html")

#Fetch webpage
soup = BeautifulSoup(page.content,"html.parser")
print(soup.prettify())