import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #支持中文字符串写入读取
input_file = open(r'c:/1.fnt','rb')
out_file = open(r'c:/2.fnt','wb')

char_id_re = re.compile(r'id=(.+?)\s')


for i in input_file:
    if 'char id=' in i:
        char_id = char_id_re.findall(str(i))
        i = i.rstrip() #去除读取字符串尾部的换行符
        s = i+" "+ "letter=\""+ unichr(int(char_id[0])) + "\"\n"
        out_file.write(s)
    else:
        out_file.write(i)
    
