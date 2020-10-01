import urllib
import requests
import re
import requests
import urllib.parse as up
from html.parser import HTMLParser


my_url = "https://pastebin.com/raw/7543p0ns"

my_url=input().strip()
res=requests.get(my_url).text.splitlines()
#print(res)


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                    print(name, "=", value)


parser = MyHTMLParser()

parser.feed(my_url)



result = []
find_it = r"<a href=[\"|'](.*?)[\"|'|\?]"
for link in res:
    domain = None

    try:
        domain =  up.urlsplit(
            re.findall(find_it,link)[0]
        ).hostname#netloc
    except:
        domain = 0
    if domain not in result and domain != 0:
        result.append(domain)
    #print(domain)

result.sort()

for domain in result:
    print(domain)
