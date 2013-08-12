import xlrd
import urllib2
import re
from bs4 import BeautifulSoup

fo = xlrd.open_workbook('c:/1.xls',formatting_info=True)
fp = open(r'c:/view_and_reply.xls','w')
s = fo.sheet_by_index(0)
k = len(s.hyperlink_list)
num = re.compile(r'(\d{1,100})')

for row in range(0,k):
    link = s.hyperlink_map.get((row,0))
    if link is None:
        url = 'No URL'
    else:
        url = link.url_or_path
        req = urllib2.Request(url)
        webpage= urllib2.urlopen(req)
        soup = BeautifulSoup(webpage.read())
        text = soup.findAll('span',{'class':'xi1'},limit=2)
        for i in range(0,2):
            text_to_find = str(text[i])
            view = re.findall(num,text_to_find)[1]
            fp.write(view+'\t')
        fp.write('\n')
        fp.flush()
        
    print url
fp.close()





