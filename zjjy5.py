import re
import urllib.request

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	return html

def getAdr(html):
	reg = r"<ul><li><div class=\"addi\">.*?<a href=(.*?)\" class="
	addressRe = re.compile(reg)
	addressList = re.findall(addressRe,str(html))
	x = 0 

	for address in addressList:
		urllib.urlretrieve(address,'%s.html' %s)
		x+=1

html = getHtml("http://www.cn-boxing.com/cls/cls_3_2.html")
print(getAdr(html))

