import sqlite3

fo = open(r'c:/dashengyi_cn.txt','r')
cx = sqlite3.connect(r'D:/反编译/sqlitebrowser_200_b1_win/locale_en.amf')
cu = cx.cursor()
cu.execute('select * from locale')
res = cu.fetchall()
i = 0
for line_txt in fo:
        seq = line_txt.split(':')
        key = seq[0].split(',')
        i = i+1
        if len(seq)>1:
            cu.execute(('update locale set value = ')
                       +('\'')+(seq[1].decode('utf-8'))
                       +('\' ')+('where key =')
                       +('\'')+(key[0])+('\''))
            print i 
            cx.commit()
            
        else:
            break

       
fo.flush()
fo.close()
