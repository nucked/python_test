import os
import re
import subprocess
import time

def walk_dir(path,topdown=True):
    isdir = os.path.isdir(path)
    if isdir:
         for root,dirs,files in os.walk(path,topdown):
             for name in files:
                 if name[-4:] == ".apk":
                     apk_unpack(os.path.join(root,name))
    else:
        apk_unpack(path)
                    
    
def apk_unpack(apk_file):
    cmd = r"aapt d badging "\
          +apk_file    
    pk_re = re.compile(r'name=\'(.+?)\'')
    
    data = subprocess.Popen(cmd, stdout=subprocess.PIPE, \
                     stderr=subprocess.PIPE, shell = True)
    li = data.stdout.readline ()
    pk_name = pk_re.findall(li)
    if len(pk_name) !=0:
        apk_pk_file.write( pk_name[0] + "\n")
        print pk_name[0]+ " is wrote"
    
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
    mkdir(r"f:\pk_name_list")
    outTxt = r"f:\pk_name_list\list"+str(t)+".txt"
    apk_pk_file = open(outTxt,"w+")
    global apk_pk_file
    print "Choose if or not input dir:\nInput \'1\' mean yes, other mean no\n"
    isInput = raw_input("")
    if isInput is "1":
        path = raw_input("input the dir:")
    else:
        print r"the apks are in F:\root\test"
        path = r"F:\root\test"
    walk_dir(path)
    print "\n=========Done========="
    print "\nYou can check the pk_name in "+outTxt
    apk_pk_file.flush()
    apk_pk_file.close()
    
