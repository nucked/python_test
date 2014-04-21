# -*- coding: cp936 -*-

rfd=file(r"F:\1.txt","r")
wfd=file(r"F:\2.txt","w")
h={}
for i in rfd:
    if not h.has_key(i):        
        h[i]=1
        
keys = h.keys()
keys.sort()
for k in keys:
    wfd.write(k)
    
rfd.close()
wfd.close()
