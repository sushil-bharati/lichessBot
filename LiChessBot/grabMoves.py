import urllib
from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

response = urlopen('https://en.lichess.org/ueXRivGiKE0e').read()
soup = BeautifulSoup(response,'html.parser')
tags1 = soup.findAll("div",class_="pgn")
searchString = str(tags1)
print(tags1)
queryString = str(12) + "[.].([a-zA-Z]{1,2})(.{0,1})([a-zA-Z]{0,2})(.{0,1})([O]{0,1})([0-9]{0,1})"
query = re.search(queryString,searchString)
found = str(query.group())
print (found)




