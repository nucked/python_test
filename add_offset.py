import re
y = re.compile(r'y=\"(.+?)\"')
in_file = open(r'c:/1.fnt','r')
out_file = open(r'c:/2.fnt','w')
for i in in_file:
    if 'page=\"0\"' in i:
        print 'find'
        j = y.findall(i)
        k = int(j[0])+1080
        print k
        w = i.replace('y="'+j[0]+'"','y="'+str(k)+'"')
        print w
        out_file.write(w)
    else:
        out_file.write(i)
        
