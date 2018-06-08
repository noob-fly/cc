import requests
import re
import json
import time
import random
from multiprocessing import Pool,Lock,Manager
import functools

# http://maoyan.com/board/4?offset=0
# 0,10,20,30,...90
MAXSLEEPTIME = 3
MINSLEEPTIME = 1
STAUS_OK = 200
MAX_PAGE_NUM = 10
SERVER_ERROR_MIN = 500
SERVER_ERROR_MAX = 600
CLIENT_ERROR_MIN = 400
CLIENT_ERROR_MAX = 500


# 1)对URL发起HTTP请求http request,得到相应的http response响应，我们所需的数据就在
# response的响应体里；
def get_one_page(URL, num_retries=5):  # http://maoyan.com/board/4?offset=0
    if num_retries == 0:
        return None
    ua_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}
    response = requests.get(URL, headers=ua_headers)
    if response.status_code == STAUS_OK:  # ok
        return response.text
    elif SERVER_ERROR_MIN <= response.status_code < SERVER_ERROR_MAX:
        time.sleep(MINSLEEPTIME)  # 这个休息的时间点需要仔细考虑一下
        get_one_page(URL, num_retries - 1)
    elif CLIENT_ERROR_MIN <= response.status_code < CLIENT_ERROR_MAX:
        # 真正好的做法是需要写日志
        if response.status_code == 404:
            print("Page not found")
        elif response.status_code == 403:
            print("Have no rights")
        else:
            pass
    return None


# 2)用正则表达式，XPath，BS4精确的获取数据；
def parse_one_page(html):
    pattern = re.compile(
        '<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="star">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    for it in items:
        yield {
            "title": it[0].strip(),
            "actor": it[1].strip(),
            "time": it[2].strip()
        }


# 3)存到本地的文件系统中或数据库中；
def write_to_file(item):
    with open("猫眼.txt", 'a', encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


# 4)控制整个爬取一页的流程
def crawl_one_page(lock,offset):
    # 拼出一个url
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    # 下载这个url
    html = get_one_page(url)
    # 解析每个页面，并且把获取到的item一个个写入文件
    for item in parse_one_page(html):
        lock.acquire()
        write_to_file(item)
        lock.release()
    time.sleep(random.randint(MINSLEEPTIME, MAXSLEEPTIME))  # 随机休息1-3秒之后，再进行下一次爬取

if __name__ == "__main__":
    manage = Manager()
    lock = manage.Lock()
    # 使用偏函数对原来的函数进行包装
    partial_craw = functools.partial(crawl_one_page,lock)
    pool = Pool(2)
    pool.map(partial_craw, [i * 10 for i in range(10)])
    pool.close()
    pool.join()


# for i in range(MAX_PAGE_NUM):
#        crawl_one_page(i*MAX_PAGE_NUM)

# parse_one_page(get_one_page("http://maoyan.com/board/4?offset=0"))
