import urllib2, urllib

def check_code(code):
    data = {"reginvcode":code, 'action' : 'reginvcodeck'}
    f = urllib2.urlopen(
        url     = 'http://cl.man.lv/register.php?',
        data    = urllib.urlencode(data)
        )
    response = f.read()
    if r"parent.retmsg_invcode('1')" in response:
        print code_two + " not valid"
    else:
        print code_two +" ok"

code_one = raw_input('input the code: ')
for i in range(97,123):
    code_two = code_one+chr(i)
    check_code(code_two)

for k in range(0,10):
    code_two = code_one+str(k)
    check_code(code_two)
    
    


