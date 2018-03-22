import re
import os
from bs4 import BeautifulSoup
import shutil

  
if __name__=='__main__':
    sourceDirPath="20180322"
    fileNames=os.listdir(sourceDirPath)
    goalFilepath = sourceDirPath+"_"+"LiTitle.txt"
    file_object = open(goalFilepath,'w',encoding='utf8')
    for fileName in fileNames:
        strFile=sourceDirPath+"/"+fileName
        textHtml=open(strFile,'r',encoding='utf8')
        InforStr= '''<a href="20180322/[{0}.html" class="list-group-item ">[]{1} </a>
                  '''.format(fileName,fileName)

        file_object.write(InforStr+'\n')

    file_object.close( )
  
    print("Job is OK")
