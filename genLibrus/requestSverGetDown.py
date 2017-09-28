import requests
import os
from bs4 import BeautifulSoup
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

curDir = os.path.dirname(os.path.abspath(__file__))
browser = webdriver.Firefox(executable_path= os.path.join(curDir , r'..//geckodriver//geckodriver-v0.19.0-win64//geckodriver.exe'))
user_agent_list = [ 
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"\
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",\
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",\
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",\
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
       ]
def getDown(itemUrl):
    headers = {'user-agent': random.choice(user_agent_list)}
    r1=requests.get(itemUrl,headers = headers)
    soup = BeautifulSoup(r1.text, 'lxml')
    td = soup.find('td',{"colspan":"2"})
    pageDownLoad = td.find('a').get('href')
    r2 = requests.get(pageDownLoad,headers = headers)
    soupDown = BeautifulSoup(r2.text, 'lxml')
    tdDown = soupDown.find('td',{"rowspan":"2","align":"center"})
    #print(tdDown)
    downURL=tdDown.find('a').get('href')
    print(downURL)
    print('正在下载：')
    browser.get(downURL)
    # rDown = requests.get(downURL,headers = headers, stream=True)
    # #print(rDown.text)
    # fileSize = len(rDown.content)
    # print("文件大小"+str(fileSize))
    # chunk_size = 1024
    # with open('123.pdf', 'wb') as fd:
    #     i=0
    #     for chunk in rDown.iter_content(chunk_size):
    #         i=i+1
    #         fd.write(chunk)
    #         print(str(i*chunk/fileSize))
   # browser.get(downURL)
    ##browser.quit()


urlList=[]
urlList.append("http://gen.lib.rus.ec/book/index.php?md5=F27BF5EAC8FB10E0C5CB599554CA6E68&open=3")

for itemUrl in urlList:
    getDown(itemUrl)
