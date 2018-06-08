import logging

import random
import sys
# 创建日志的实例
import urllib.request

import time

logger = logging.getLogger("basicSpider")

# 定制Logger的输出格式
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

# 创建日志:文件日志,终端日志
file_handler = logging.FileHandler('basicSpider.log')
file_handler.setFormatter(formatter)

consle_handler = logging.StreamHandler(sys.stdout)
consle_handler.setFormatter(formatter)

# 设置默认的日志级别
logger.setLevel(logging.INFO)

# 把文件日志和终端日志添加到日志处理器中
logger.addHandler(file_handler)
logger.addHandler(consle_handler)


def downloadHtml(url, headers=[], proxy={}, num_retries=10, timeout=10, decodeInfo="utf-8"):
    """
    爬虫的get请求,考虑了UA等http request head 部分的设置:
    支持代理服务器的信息处理
    返回的状态码不是200,这时怎么处理:
    考虑超时问题,以及网页的编码问题
    """
    html = None
    # logger.debug("download starting")
    # logger.debug("download completed")
    # 一般来说,使用UA池和代理服务器Proxy池相结合的方式来访问某个页面,会更加的不容易反爬
    # 动态的调整代理服务的使用策略
    if random.randint(1, 10) >=1:
        proxy = None

    proxy_handler = urllib.request.ProxyHandler(proxy)
    # 替换handler,以实现可以处理proxy
    opener = urllib.request.build_opener(proxy_handler)

    # 把 opener 装载进urllib库中,准备使用
    opener.addheaders = headers
    urllib.request.install_opener(opener)
    try:
        response = urllib.request.urlopen(url) # 爬取网页
        html = response.read().decode(decodeInfo) #读取网页内容
    except UnicodeDecodeError:
        logger.err("UnicodeDecodeError")
    except urllib.error.URLError or urllib.error.HTTPError as e:
        logger.error("urllib error")
        if hasattr(e,"code") and 400 <= e.code < 500:
            logger.error("Client Error")
        elif hasattr(e,'code') and 500<= e.code <600:
            html = downloadHtml(url,headers,proxy,timeout,decodeInfo,num_retries-1) # 若失败则再次爬取网页
            time.sleep(2)
    except:
        logger.error("down erroe")
    return html

if __name__ == "__main__":
    url = "http://baidu.com"
    headers = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]
    proxy = {"http": "123.201.46.196:80"}
    print(downloadHtml(url,headers,proxy))
    logger.removeHandler(file_handler)
    logger.removeHandler(consle_handler)
