from bs4 import BeautifulSoup, SoupStrainer
import requests
from subprocess import call
import os

if not os.path.exists("pdfs"):
	os.mkdir("pdfs")

s = requests.Session()
url = "https://people.rit.edu/vxnsps/viv.html"
pre = "https://people.rit.edu/vxnsps/"
resp = s.get(url)
txt = resp.text
soup = BeautifulSoup(txt,"lxml")
for link in soup.find_all('a',href=True):
	print link['href']
	if link['href'].endswith("pdf"):
		call(["wget","-P","pdfs/",pre+link['href']])

		
