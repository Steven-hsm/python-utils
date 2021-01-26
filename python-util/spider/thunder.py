import sys

import requests
from bs4 import BeautifulSoup
sys.path.append('../utils')
import fileutils

videoUrl = "http://www.dy1234.net/sub/14297.html"

originalHtml = requests.get(videoUrl).text
#编解码
html = originalHtml.encode("ISO-8859-1")
html = html.decode("gb18030")

soup = BeautifulSoup(html, 'html.parser')

downloadUrls = soup.select("input.down_url")

#获取value属性
for url in downloadUrls:
    fileutils.writeToFile("1.txt",url.get("value")+"\n")
    print(url.get("file_name") + "\t" + url.get("value"))



