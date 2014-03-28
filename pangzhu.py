#coding:utf-8

import urllib2
import json


header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}  
url_input = raw_input(u"请输入要查询的网址:")
url = 'http://domains.yougetsignal.com/domains.php?remoteAddress='
url_search = url + url_input


req = urllib2.Request(url_search,headers = header)
html_source = urllib2.urlopen(req)
json_source = html_source.read()
json_decode = json.loads(json_source)

search_stat = json_decode['status']
domain_list = json_decode['domainArray']
search_ip = json_decode['remoteIpAddress']
domain_Count = json_decode['domainCount']

if search_stat == 'Success':
    print u'网址ip为:', search_ip
    print u'域名总计有:',domain_Count 
    print u'列表如下:'
    for domain in domain_list:
        print domain[0]
