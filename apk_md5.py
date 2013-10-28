# -*- coding: cp936 -*-
import os
import re
import subprocess
import time
from hashlib import md5

def walk_dir(path,topdown=True):
    isdir = os.path.isdir(path)
    if isdir:
         for root,dirs,files in os.walk(path,topdown):
             for name in files:
                 if name[-4:] == ".apk" or name[-4:] == "odex":
                     apk_md5sum(os.path.join(root,name))
    else:
        apk_md5sum(path)
                    
    
def apk_md5sum(apk_file):
    apk_md5 = md5_file(apk_file)
    apk_md5_file.write(apk_md5+"    "+apk_file+"\n")
    

def md5_file(name):
    m = md5()
    a_file = open(name, 'rb')    #需要使用二进制格式读取文件内容
    m.update(a_file.read())
    a_file.close()
    return m.hexdigest()
    
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)
        print path+" create OK \n"
        return True
    else:
        return False

if __name__ == '__main__':    
    t = time.time()
    mkdir(r"f:\system_md5")
    outTxt = r"f:\system_md5\md5"+str(t)+".txt"
    apk_md5_file = open(outTxt,"w+")
    global apk_md5_file
    print "Choose if or not input dir:\nInput \'1\' mean yes, other mean no\n"
    isInput = raw_input("")
    if isInput is "1":
        path = raw_input("input the dir:")
    else:
        path = r"F:\rom\华凌\system\app"
    walk_dir(path)
    print "\n=========Done========="
    print "\nYou can check the md5 in "+outTxt
    apk_md5_file.flush()
    apk_md5_file.close()
    
