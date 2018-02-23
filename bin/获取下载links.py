#author:wr786
import urllib.request
import re

url = input("请输入恁要下载的小说的网址:")
response = urllib.request.urlopen(url)
data = response.read().decode('gb2312','ignore')
pattern = re.compile(r'<li><a href=\'(.*?)\' target="_blank">(.*?)</a></li>')
items = re.findall(pattern,data)
f = open('.\links.txt','w')
for item in items:
    f.write("http://www.ting89.com" + item[0] + " by" + item[1] + "\n")
f.close()
