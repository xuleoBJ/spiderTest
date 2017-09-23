from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup



browser = webdriver.Firefox(executable_path=r'..//geckodriver//geckodriver-v0.19.0-win64//geckodriver.exe')

def getDown(itemUrl):
    browser.get(itemUrl)
    html = browser.page_source
    soup = BeautifulSoup(html, 'lxml')
    td = soup.find('td',{"colspan":"2"})
    pageDownLoad = td.find('a').get('href')
    browser.get(pageDownLoad)
    htmlDown = browser.page_source
    soupDown = BeautifulSoup(htmlDown, 'lxml')
    tdDown = soupDown.find('td',{"rowspan":"2","align":"center"})
    #print(tdDown)
    downURL=tdDown.find('a').get('href')
    print(downURL)
    browser.get(downURL)
    ##browser.quit()


urlList=[]
urlList.append("http://gen.lib.rus.ec/book/index.php?md5=3BD277D29365DB7223A18E86463CA718&open=3")

for itemUrl in urlList:
    getDown(itemUrl)
