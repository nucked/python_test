# -*- coding: cp936 -*-
import os
import zipfile

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
    zipFile = zipfile.ZipFile(apk_file)
    for lib in zipFile.namelist():
        if lib[:4] == r"lib/":
            i = len(apk_file.split("\\"))
            pw = apk_file.split("\\")
            outDir = ""
            for k in range(0,i-1):
                outDir = outDir + pw[k]+"\\"
            print outDir
            zipFile.extract(lib, outDir)  
        
    
    

if __name__ == '__main__':    
    path = r"F:\rom\"
    walk_dir(path)
    print "\n=========Done========="
    
