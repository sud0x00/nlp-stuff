import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
myurl = "http://www.brainjar.com/java/host/test.html"
html = urlopen(myurl).read()
s = BeautifulSoup(html, "html.parser")
print(s.get_text().strip())
