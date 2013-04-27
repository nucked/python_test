import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def fnt_read(a,b,c,d,e,f,g):
    char_id = a
    x = b
    y = c
    width = d
    height = e
    xoffset = f
    yoffset = g

    fnt_line = (r'Char="'+unichr(int(char_id))+r'",'+x+r','+y+r','
                +width+r','+height+r','+xoffset+r','
                +yoffset+'\n')
    return fnt_line

fnt = open (r'c:\3.fnt','r')
fnt_bak = open (r'c:\2x_font_STD.fnt','w')
char_id_re = re.compile(r'id=(.+?)\s')
x = re.compile(r'x=(.+?)\s')
y = re.compile(r'y=(.+?)\s')
width = re.compile(r'width=(.+?)\s')
height = re.compile(r'height=(.+?)\s')
xoffset= re.compile(r'xoffset=(.+?)\s')
yoffset= re.compile(r'yoffset=(.+?)\s')
for i in fnt:
    if 'char id=' in i:
        char_id = char_id_re.findall(str(i))
        char_x = x.findall(str(i))
        char_y = y.findall(str(i))
        char_width = width.findall(str(i))
        char_height = height.findall(str(i))
        char_xoffset = xoffset.findall(str(i))
        char_yoffset = yoffset.findall(str(i))
        fnt_line =fnt_read(char_id[0],char_x[0],char_y[0],char_width[0],
                 char_height[0],char_xoffset[0],
                 char_yoffset[0])
        fnt_bak.write(fnt_line)
fnt.close()
fnt_bak.close()

