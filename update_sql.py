import sqlite3

fo = open(r'c:/dashengyi.txt','w')
cx = sqlite3.connect(r'D:/反编译/sqlitebrowser_200_b1_win/locale_en.amf')
cu = cx.cursor()
cu.execute('select * from locale')
res = cu.fetchall()

cu.execute(('update locale set value = ')+(' \' 否\' where key = \'No\''))
cx.commit()

for line in res:
    fo.write(line[0].encode('utf-8')+','+line[1].encode('utf-8')+':\n')

fo.flush()
fo.close()
