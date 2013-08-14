import re

smali =  open(r'c:/3.smali','r')
smali_bak = open(r'c:/4.smali','wb')
mark = 0
for word in smali:
    j = word.decode('utf-8')
    for i in j:        
        k = ord(i)
        if k<=128:
            smali_bak.write(i)
            continue
        for x in unichr(k).encode('utf-8'):
            smali_bak.write( hex(ord(x)) + 't\n')
         
            

smali.close()
smali_bak.close()   
