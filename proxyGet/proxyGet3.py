# -*- coding: gbk -*-
from bs4 import BeautifulSoup
import urllib.request
import threading
import sys
import requests

inFile = open('E:\\spiderTest\\proxyGet\\proxy.txt')
outFile = open('verified.txt', 'w')
lock = threading.Lock()

def getProxyList(targeturl="http://www.xicidaili.com/nn/"):
    countNum = 0
    proxyFile = open('proxy.txt' , 'a')
    
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    
    
    for page in range(1, 10):
        url = targeturl + str(page)
        #print url
        #request = urllib.Request(url, headers=requestHeader)
        req = urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
        html_doc = urllib.request.urlopen(req).read()
    
        soup = BeautifulSoup(html_doc, "html.parser")
        #print soup
        table= soup.find('table', id='ip_list')
        for tr in table.findAll('tr'):
                tds = tr.find_all('td')
                if len(tds)>9:
                    #国家
                    if tds[0].find('img') is None :
                        nation = '未知'
                        locate = '未知'
                    else:
                        nation =   tds[0].find('img')['alt'].strip()
                        locate  =   tds[3].text.strip()
                    ip      =   tds[1].text.strip()
                    port    =   tds[2].text.strip()
                    anony   =   tds[4].text.strip()
                    protocol=   tds[5].text.strip()
               #     speed   =   tds[5].find('div')['title'].strip()
                    time    =   tds[8].text.strip()
                    
                    if verifyProxy(ip,port,protocol):
                        proxyFile.write('%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol, time) )
                        countNum += 1
                        print ('%s=%s:%s is ok' % (protocol, ip, port))
                    else:
                        print ('%s=%s:%s is not ok' % (protocol, ip, port))
    
    proxyFile.close()
    return countNum

def verifyProxy(ip,port,protocol):
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    myurl = 'http://www.baidu.com/'
    ipProxy = protocol+':'+ip+':'+port
    print (ipProxy)
    try:
        r = requests.get(myurl,headers=requestHeader,proxies={protocol:ip+':'+port},verify=True,timeout=6)
        if  r.status_code == 200:
            return 1
        else:
            return 0
    except error.urlError as e:
        print(e.reason)
        return 0
    
def verifyProxyList():
    '''
    验证代理的有效性
    '''
    requestHeader = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    myurl = 'http://www.baidu.com/'

    while True:
        lock.acquire()
        ll = inFile.readline().strip()
        lock.release()
        if len(ll) == 0: break
        line = ll.strip().split('|')
        protocol= line[5]
        ip      = line[1]
        port    = line[2]
        
        try:
            conn = httplib.HTTPConnection(ip, port, timeout=5.0)
            conn.request(method = 'GET', url = myurl, headers = requestHeader )
            res = conn.getresponse()
            lock.acquire()
            print ("+++Success:" + ip + ":" + port)
            outFile.write(ll + "\n")
            lock.release()
        except:
            print ("---Failure:" + ip + ":" + port)
        
    
if __name__ == '__main__':
    tmp = open('E:\\spiderTest\\proxyGet\\proxy.txt' , 'w')
    tmp.write("")
    tmp.close()
    proxynum = getProxyList("http://www.xicidaili.com/nn/")
    print (u"国内高匿：" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/nt/")
    print (u"国内透明：" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/wn/")
    print (u"国外高匿：" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/wt/")
    print (u"国外透明：" + str(proxynum))

    print (u"\n验证代理的有效性：")
    
##    all_thread = []
##    for i in range(30):
##        t = threading.Thread(target=verifyProxyList)
##        all_thread.append(t)
##        t.start()
##        
##    for t in all_thread:
##        t.join()
##    
##    inFile.close()
##    outFile.close()
    print ("All Done.")
