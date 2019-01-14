import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup as soup
#抓取整个网页
def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = data.decode('utf-8')
    return data

url = 'http://www.mcfly.com.cn/mcloud/api'

all_html = getHtml(url)
#
# with open('mcfly.txt','w') as f:
#     f.write(all_html)
print(all_html.a)

