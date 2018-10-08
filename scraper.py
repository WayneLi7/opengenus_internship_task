import urllib2
from bs4 import BeautifulSoup
import sys

def get_same_domain_links(url):
	try:
		response = urllib2.urlopen(url)
	except urllib2.HTTPError, e:
    		print(e.getcode())
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	##find all <a> tag
	a_tags = soup.find_all('a')
	link_count = 0
	##get hostname
	search_domain = urllib2.urlparse.urlparse(url).hostname
	for a_tag in a_tags:
		link = a_tag.get('href')
		##if it is a internal link or it is a hyperlink points to same host
		if search_domain in link or ("http" not in link and "/" in link):
			print(a_tag.get('href'))
			link_count += 1
	return (len(html), link_count)

if __name__ == "__main__":
    print(get_same_domain_links(sys.argv[1]))


