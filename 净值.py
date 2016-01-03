import re
import requests
html = requests.get("http://fund.eastmoney.com/f10/F10DataApi.aspx?type=lsjz&code=000070&page=2&per=20&sdate=&edate=")
html.encoding = 'GB2312'
print html.text
info = '<tr><td>(?<日期>\d.+?)</td><td class='tor bold'>(?<单位净值>\d.+?)</td><td class='tor bold'>(?<累计净值>\d.+?)</td><td class='tor bold (?<涨跌>.+?)'>(?<日增长率>.+?)</td><td>(?<申购状态>.+?)</td><td>(?<赎回状态>.+?)</td><td class='red unbold'>(?<分红配送>.*?)</td></tr>'
getinfo = re.findall(info,html.text)
for x in getinfo:
    print x