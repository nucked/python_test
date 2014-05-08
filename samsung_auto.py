# -*- coding: cp936 -*-
import os
import re
import subprocess
import time
import csv
import sys

def walk_dir(path,topdown=True):
    isdir = os.path.isdir(path)
    if isdir:
         for root,dirs,files in os.walk(path,topdown):
             for name in files:
                 if name[-4:] == ".apk":
                     apk_unpack(os.path.join(root,name))
                 elif name[-4:] == ".txt":
                     txt_parse(os.path.join(root,name))
                 else:
                     print "not found method matched"
    else:
        apk_unpack(path)
                    
    
def apk_unpack(apk_file):
    cmd = r"aapt d badging "+apk_file    
    pk_re = re.compile(r'name=\'(.+?)\'')
    lb_re = re.compile(r'application:\slabel=\'(.+?)\'')
    apk_name = apk_file.split("\\")
    k = len(apk_name)
    apk_dir = ""
    for i in range(5,k):
        apk_dir = apk_dir + "/" + apk_name[i]
    
    data = subprocess.Popen(cmd, stdout=subprocess.PIPE, \
                     stderr=subprocess.PIPE, shell = True)
    li = data.stdout.readline ()
    pk_name = pk_re.findall(li)
    ai = data.stdout.read()
    app_name = lb_re.findall(ai)
    #print pk_name,app_name

    
    if len(pk_name) !=0 and len(app_name) !=0:
        #data = ["/system/app/" + apk_name[-1],pk_name[0],app_name[0]]
        #writer = csv.writer(apk_pk_file)
        #writer.writerow(data)
        data = "/system/preload/" + apk_name[-1] + "," + pk_name[0] + "," + app_name[0]+"\n"
        apk_pk_file.write(data)
        print data

def txt_parse(packages_txt):
    f = open(packages_txt,"r")
    pk_re = re.compile(r'name=\'(.+?)\'')
    apk_name = packages_txt.split("\\")
    yuquan_txt = apk_name[-1]
    if yuquan_txt[0] == "z":
        for i in f:
            pk_name = pk_re.findall(i)
            if len(pk_name)>0:
                for j in range(0,len(pk_name)):
                    apk_pk_file.write("\n"+pk_name[j])
    else:
        for k in f:
            pk_name = k.split(" : ")
            if len(pk_name)>1:
                apk_pk_file.write(pk_name[1])   
    
    
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
    #mkdir(r"f:\pk_name_list")
    #outTxt = r"f:\pk_name_list\list"+str(t)+".txt"
    print "Choose if or not input dir:\nInput \'1\' mean yes, other mean no\n"
    isInput = raw_input("")
    if isInput is "1":
        path = raw_input("input the dir:")
    else:
        path = r"G:\三星\s7572"
        print r"the apks are in "+path
    outTxt = path+r"\list.csv"
    apk_pk_file = open(outTxt,"w+")
    global apk_pk_file  
    walk_dir(path)
    print "\n=========Done========="
    print "\nYou can check the pk_name in "+outTxt
    apk_pk_file.flush()
    apk_pk_file.close()
    
