import urllib.request
import re
from lxml import etree
url = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')

pattern = re.compile(
    '<li><a target="_blank" ' 'href="http://www.cninfo.com.cn/information/companyinfo_n.html\?fulltext\?(.*?)">')
data = re.findall(pattern,html)
print(len(data)) #3639
url = 'http://www.cninfo.com.cn/information/management/'
fallurl = []
for i in data:
    fallurl1 = url + i + '.html'
    fallurl.append(fallurl1)
#print(new_url)
#print(new_url)
for new_url in fallurl:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    request = urllib.request.Request(new_url,headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('gbk')
    #print(html)
    text = etree.HTML(html)
    titles = text.xpath('//div[@class="clear"]/*/tr')
    for n in range(2,len(titles)):
        titles = text.xpath('//div[@class="clear"]/*/tr[%d]/td/text()'%n)
        info = titles[0].replace('\r\n ','')+':'+ ','.join([name.strip('\n\r ') for name in titles[1:]])+ '\n'
        with open('info.text','a') as f:
            f.write(info)


