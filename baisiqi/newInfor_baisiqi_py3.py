import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
fileWrited=open("new.txt",'w',encoding="utf8")
for i in range(1,1300):
    pageStrUrl = "http://www.100siqi.com/showcom.asp?id="+str(i)
    page  = requests.get(pageStrUrl,headers = headers)

    print("商户"+str(i))
    fileWrited.write("商户"+str(i))
    soup = BeautifulSoup(page.content,'html.parser') # 按照html格式解析页面
    inforGet = soup.find_all(class_ ='basic-info')
    print (inforGet)
    if i%50 != 0:
        fileWrited.write(str(inforGet))
    else:
        fileWrited.close()
        fileWrited=open(str(i)+"new.txt",'w',encoding="utf8")

fileWrited.close()
