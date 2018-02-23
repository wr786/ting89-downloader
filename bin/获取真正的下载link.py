#author:wr786
import urllib.request
import re
import os
import time
from selenium import webdriver

abspath = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")  
browser = webdriver.Chrome(abspath)

resource = open(".\links.txt","r")
urls = resource.readlines()
output = open(".\output\link.txt","w")

for eachline in urls:
    cur = eachline.find(" by")
    url = eachline[:cur] 
    name = eachline[cur+3:]

    browser.get(url)
    data = browser.page_source
        
    pattern = re.compile(r'<iframe src=.*?url=(.*?)".*?height.*?></iframe>')
    source = re.findall(pattern,data)
    for eachsource in source:
        output.write(eachsource + '\n')
    
    #for each in source:
    #    rsp = urllib.request.urlopen(each)
    #    of = open(".\\output\\" + name + ".mp3","wb")
    #    of.write(rsp.read())
    #    of.close()
    #    printf(name + "下载成功")
    
browser.close()
resource.close()
output.close()
