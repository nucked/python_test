import re
text_re = re.compile(r'":"(.+?)"')

fp = open (r'c:/database.txt','r')
fo = open (r'c:/database_text.txt','w')
for line in fp.readlines():
    text = text_re.findall(line)
    if len(text) != 0:
        for i in range(0,len(text)):
            if i != 0:
                fo.write(text[i].strip()+'\n')
            else:
                fo.write(text[i]+'\n')

        fo.write("\n####### END #######\n\n")
            
fo.flush()
fo.close()
