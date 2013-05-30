import webbrowser

def num_to_link(num):
    if num == '':
        return ''
    anzhi_link_1 = r'http://bbs.anzhi.com/thread-'
    anzhi_num = num
    anzhi_link_2 = r'-1-1.html'
    anzhi = anzhi_link_1 + anzhi_num + anzhi_link_2
    return anzhi
    


s = raw_input(r'请输入要打开链接文本位置: ')
print r'文本为: ' +s

link = open(s,'r')
test = open(r'c:/test.txt','w')


for i in link:
    i = i.rstrip() 
    webbrowser.open(num_to_link(i))
