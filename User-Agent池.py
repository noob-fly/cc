import random
import requests
import time

l = [
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'},
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0'},
    {'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'},
    {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER) '}
]
for i in range(1,11):
    m =int(random.random()*20)
    print(m)
    headers = l[m]
    print(headers)
    response = requests.get('http://www.sina.com.cn',params=None,headers=headers)
    response.encoding = 'utf-8'
    # print(response)
    time.sleep(int(random.random()*2+1))


#print(response.util("User-Agent"))
# with open('sina.html','w') as f:
#     f.write(response.text)
# from urllib import request
# req = request.Request("http://www.sina.com.cn") # 构造ｒｅｑｕｅｓｔ请求
# response = request.urlopen(req) # 得到ｒｅｑｕｓｅｔ相应信息
# print(type(response.read()))   # <class 'bytes'>
# print(response.read().decode("utf-8"))

# def info(object,collapse=0,spacing=20):
#     # 打印object中可以被调用的方法信息
#     methodlist = [method for method in dir(object) if callable(getattr(object,method))]
#     # print(methodlist)
#     # print(''.join("%s"%[str(method.ljust(spacing)) for method in methodlist]))
#     #[ '__add__             ', '__class__           ', '__contains__        ', '__delattr__         ', '__dir__  ]
#     processFun = collapse and (lambda s:"".join(s.split())) or (lambda s:s)
#     # print(''.join("%s" %[processFun(str(getattr(object,method).__doc__)) for method in methodlist]))
#     print('\n'.join(["%s %s" % (str(method.ljust(spacing)),processFun(str(getattr(object,method).__doc__))) for method in methodlist]))
# s = 'str'
# info(s)
# help(list)
# def maxmin(l,start,end): # 求一个列表的最大最小值
#     if start - end <= 0:
#         return (max(l[start],l[end]),min(l[start],l[end]))
#     else:
#         max1,min1 = maxmin(l,start,(start+end)//2)
#         max2,min2 = maxmin(l,(start+end)//2+1,end)
#         return (max(max1,max2),min(min1,min2))
# l = [1,2,3,-1,-5,9,32,-12,34]
# maxv,minv = maxmin(l,0,len(l)-1)
# print(maxv,minv)
