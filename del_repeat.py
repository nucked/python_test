import re
text_re = re.compile(r'":"(.+?)"')

fp = open (r'c:/database_text.txt','r')
fo = open (r'c:/database_out.txt','w')
allLine = fp.readlines()
h = {}

for line in allLine:
    if not h.has_key(line):
        h[line]=1
        fo.write(line)
    elif "####### END #######" in line or '\n' == line :
        fo.write(line)
            
fo.flush()
fo.close()
