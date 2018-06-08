from pachong.laji.basicspider import downloadHtml
from bs4 import BeautifulSoup
import re
from multiprocessing import Pool,Manager
def get_html(url,headers,proxy):
    html = downloadHtml(url,headers=headers,proxy=proxy)
    return html
def get_move_detail(html):
    soup = BeautifulSoup(html,'html.parser')
    move_list = soup.find_all('div',class_="bd doulist-subject")
    return move_list
def get_move_one(movie):
    result = ''
    soup = BeautifulSoup(str(movie),'html.parser')
    title = soup.find_all('div',class_='title')
    soup_title = BeautifulSoup(str(title[0]),'html.parser')
    for line in soup_title.stripped_strings:
        result += line
    try:
        score = soup.find_all('span',class_ ='rating_nums')
        soup_score = BeautifulSoup(str(score[0]), 'html.parser')
        for line in soup_score.stripped_strings:
            result += "||　评分："
            result += line
    except:
        result += "||　评分：　5.0"
    abstract = soup.find_all('div', class_='abstract')
    soup_abstract = BeautifulSoup(str(abstract[0]), 'html.parser')
    for line in soup_abstract.stripped_strings:
        result += "||　摘要："
        result += line
    result += "\n"
    return result
def save_file(movieinfo,lock):
    with open("doubamMovie.text","a") as f:
        f.write(movieinfo)
def crawMovieInfo(url,headers,proxy,q,lock):
    html = get_html(url, headers, proxy)
    movie_list = get_move_detail(html)
    for it in movie_list:
        result = get_move_one(it)
        save_file(result,lock)
    q.put(url) #　已完成的url

if __name__ == "__main__":
    pool = Pool()# 进程池
    q = Manager().Queue() # 进程池队列
    lock = Manager().Lock()
    url = "https://www.douban.com/doulist/3516235/?start=225&sort=seq&sub_type="
    headers = [('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')]
    proxy = {"https": "139.199.230.242:1080"}
    crawMovieInfo(url,headers,proxy,q,lock )
    html = get_html(url,headers,proxy)
    pattern = re.compile('(https://www.douban.com/doulist/3516235/\?start=.*)"')
    itms = re.findall(pattern,html)
    print(itms)
    craw1_queue =[] # 待爬
    crawed_queue = [] #  已爬
    for itm in itms:
        if itm not in crawed_queue: #第一步去重，确认不再已爬队列中
            craw1_queue.append(itm)
    craw1_queue = list(set(craw1_queue))
    # 模拟广度优先遍历
    while craw1_queue: # 去待爬队列中去取ｕｒｌ．直到为空
        url = craw1_queue.pop(0)# 去出待爬队列中的第一个值
        crawMovieInfo(url,headers,proxy,q,lock)
        # 把已经处理的url放到已经爬取打队列中
        crawed_queue.append(url)
    print(len(crawed_queue))
    pool.close()
    pool.join()

# re：(div class="title">[\s\S]*?>([\s\S]*?</a>[\s\S]*?<span class="rating_nums">([\s\S]*?)</span>[\s\S]*?<div class="abstract">([\s\S]*?)<br/>([\s\S]*?)<br/>)
