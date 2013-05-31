import re

smali = open(r'c:/AboutActivity.smali','r')
smali_bak = open(r'c:/AboutActivity.txt','w')
char_id_re = re.compile(r'0x(.+?)t')
j = 0
for i in smali:
    j= j+1
    char_id = char_id_re.findall(i)
    
    if len(char_id) != 0:
        print j
        smali_bak.write(chr(int(char_id[0],16)))
        
    else:
        if r'.end array-data' in i:
            smali_bak.write('\n'+i)
        else:
            smali_bak.write(i)

print 'Done'
        
    
    
    
