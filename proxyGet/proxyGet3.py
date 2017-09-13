# -*- coding: gbk -*-
from bs4 import BeautifulSoup
import urllib.request
import threading
import sys


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
        trs = soup.find('table', id='ip_list').find_all('tr')
        for tr in trs[1:]:
            tds = tr.find_all('td')
            #����
            if tds[1].find('img') is None :
                nation = 'δ֪'
                locate = 'δ֪'
            else:
                nation =   tds[1].find('img')['alt'].strip()
                locate  =   tds[4].text.strip()
            ip      =   tds[2].text.strip()
            port    =   tds[3].text.strip()
            anony   =   tds[5].text.strip()
            protocol=   tds[6].text.strip()
            speed   =   tds[7].find('div')['title'].strip()
            time    =   tds[9].text.strip()
            
            proxyFile.write('%s|%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol,speed, time) )
            #print '%s=%s:%s' % (protocol, ip, port)
            countNum += 1
    
    proxyFile.close()
    return countNum
    
def verifyProxyList():
    '''
    ��֤��������Ч��
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
    print (u"���ڸ��䣺" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/nt/")
    print (u"����͸����" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/wn/")
    print (u"������䣺" + str(proxynum))
    proxynum = getProxyList("http://www.xicidaili.com/wt/")
    print (u"����͸����" + str(proxynum))

    print (u"\n��֤��������Ч�ԣ�")
    
    all_thread = []
    for i in range(30):
        t = threading.Thread(target=verifyProxyList)
        all_thread.append(t)
        t.start()
        
    for t in all_thread:
        t.join()
    
    inFile.close()
    outFile.close()
    print ("All Done.")