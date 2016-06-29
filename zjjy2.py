import urllib.request
import time
import webbrowser as web #假名,看第7行
import os
url = "http://blog.sina.com.cn/s/blog_738ab0e60102vnl4.html"
i = 0 
while True:
	web.open_new_tab(url)
	i += 1
	time.sleep(1.8)
	content = urllib.request.urlopen(url).read()
	print(content)
	if	i%6 == 0:
		os.system("taskkill /F /IM Maxthon.exe")