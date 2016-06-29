import urllib.request
import webbrowser as web #假名,看第7行
url = "http://www.163.com"
content = urllib.request.urlopen(url).read()
print(content)
open("163.com.html","wb").write(content) #写入2进制
web.open_new_tab("163.com.html") #webbrowser.open_new_tab("163.com.html")