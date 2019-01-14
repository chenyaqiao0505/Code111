# import requests
# from bs4 import BeautifulSoup
#
#
# siteAddress = 'http://www.dangdang.com/?_ddclickunion=362-A100232543jiangkang%7C2578072480009B%5E20190107142246-80508%7C99999%7C01%7C|ad_type=0|sys_id=1#dd_refer=http%3A%2F%2Fnclick.linktech.cn%2F%3Fm%3Ddangdang%26a%3Da100232543%26l%3D99999%26l_cd1%3D0%26l_cd2%3D1%26u_id%3Djiangkang%26tu%3Dhttp%253a%252f%252fwww.dangdang.com%26url%3Dhttp%3A%2F%2Fwww.dangdang.com'
#
# r = requests.get(siteAddress)
#
# soup = BeautifulSoup(r.text)
#
# for link in soup.find_all('li',class_ ='n_b'):
#     print(link.contents,len())
#     # soup.find_all(link.contents,'dd_name')

import requests

webSite = 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F'
r = requests.post(webSite,data={'chenyaqiao666','qq819384238!'})
