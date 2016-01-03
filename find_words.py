# a = 'xz123'
# b = re.findall('x.',a)
# print b

# a = 'xyxy123'
# b = re.findall('x*',a)
# print b

# a = 'xzxzxzx123\
#     xsx'
#
# b = re.findall('x(.*?)x',a,re.S)
# print b

# coding=UTF-8
import requests
import re
html = requests.get("http://fund.eastmoney.com/000001.html")
html.encoding = 'GB2312'
# print html.text
info = '<li class="rq">(\d.+?)</li><li class="dwjz"><span class="ping">(.+?)</span></li><li class="ljjz"><span class="ping">(.+?)</span></li><li class="zdf"><span class="zdf(.+?)">(.+?)</span></li>'
getinfo = re.findall(info,html.text)
for x in getinfo:
    print x
# out = open("html.html",'w')
# out.write(html.text.encode('GB2312'))
# out.close()
