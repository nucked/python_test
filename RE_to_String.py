import re
import os

def walk_dir(dir,topdown=True):
    for root,dirs,files in os.walk(dir,topdown):
        for name in files:
            smali_to_char(os.path.join(root,name))

def smali_to_char(name):
    smali = open(name,'r')
    smali_bak = open(name+'bak','w')
    char_id_re = re.compile(r'0x(.+?)t')
    j = 0
    for i in smali:
        j= j+1
        char_id = char_id_re.findall(i)
    
        if len(char_id) != 0 and (r'sswitch' not in i):
            smali_bak.write(chr(int(char_id[0],16)))
        
        else:
            if r'.end array-data' in i:
                smali_bak.write('\n'+i)
            else:
                smali_bak.write(i)
    print 'Done'

path = r'c:/smali'
walk_dir(path)


        
    
    
    
