import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

for i in range(1,10):
    pageStrUrl = "http://www.57060.com/item.php?act=list&catid=38&aid=0&type=normal&num=40&total=407&page="+str(i)
    page  = requests.get(pageStrUrl,headers = headers)

    print(page .status_code)

    soup = BeautifulSoup(page.content,'html.parser') # 按照html格式解析页面
    print (soup.find_all(class_ ='info'))
