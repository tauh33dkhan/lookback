import sys
import urllib
from bs4 import BeautifulSoup
import re

target = sys.argv[1]
url = "http://web.archive.org/cdx/search/cdx?url=http://"+target+"/*&output=text&f1=original&collapse=urlkey" 
print "[+] Collecting Url's From Wayback Machine"
query = urllib.urlopen(url)
soup = BeautifulSoup(query, 'html.parser')
str_data = str(soup)
data = re.findall(r'(https?://\S+)',str_data)

for urls in data:
	print urls

