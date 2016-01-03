import re
import requests
html = requests.get("http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=000070&page=2&per=20&sdate=&edate=")
html.encoding = 'GB2312'
# print html.text
info = '<tr><td>(\d.+?)</td><td class=\'tor bold\'>(\d.+?)</td><td class=\'tor bold\'>(\d.+?)</td><td class=\'tor bold (.+?)\'>(.+?)</td><td>(.+?)</td><td>(.+?)</td><td class=\'red unbold\'>(.*?)</td></tr>'
getinfo = re.findall(info,html.text)
for x in getinfo:
    for t in x:
        print t