import urllib
import re

from urllib.request import urlopen

#connect to a URL
# website = urllib2.urlopen(url)
website = urlopen("https://www.wp.pl/")

#read html code
html = website.read()

#use re.findall to get all the links

html = html.decode('ISO-8859-1')  #  in new version in Python i have to add this line in order to encode
links = re.findall('"((http|ftp)s?://.*?)"', html)

# print(links)

for link in links: #it's better than show all links together in one long line
    print(link)