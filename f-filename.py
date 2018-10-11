#!/usr/bin/python
# encoding: utf-8

import os,os.path,time  #file ,path ,time
import shutil  #copy file
from datetime import datetime, timedelta #datetime

def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ") # 分割为数组
    # print(exts)
    files = os.listdir(dir) # return a list containing names of the entries in the directory
    for name in files:
        fullname = os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                print(os.path.getctime(fullname))  # change time ,metadata ,seconds
                fileCtime = time.ctime(os.path.getctime(fullname))  
                print(fileCtime) # local time string 
                fileDatetime = datetime.strptime(fileCtime,"%a %b %d %H:%M:%S %Y")
                print(fileDatetime) # datetime
                boolDatetime = fileDatetime > datetime(2018,10,4)
                #&  (time.ctime(os.path.getctime(name)) > datetime(2018,10,4))
                if(name.endswith(ext) & boolDatetime  ): 
                    print(boolDatetime)
                    file.write(name + time.ctime(os.path.getctime(fullname)) + "\n")
                    file.write(os.path.join(dir,name) + "\n")
                    shutil.copy2(os.path.join(dir,name), '/Users/liutong/Downloads/oss')
                    break

def Test():
    dir="/Users/liutong/Desktop"     #文件路径
    outfile="binaries.txt"                     #写入的txt文件名
    wildcard = ".jpg .txt .png .dll .lib .xlsx"      #要读取的文件类型；空格隔开

    file = open(outfile,"w")  # open a file (if doesn't exist then creat) with write mode
    if not file:
        print ("cannot open the file %s for writing" % outfile)

    if file is not None:
        print ("open the file %s for writing" % outfile)  

    if file is None:
        print ("cannot open the file %s for writing" % outfile)

    ListFilesToTxt(dir,file,wildcard, 1)

    file.close()


Test()
