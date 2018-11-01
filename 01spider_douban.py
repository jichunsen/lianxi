

import requests
import re
1.增加
def get_html(url):

    response=requests.get(url)

    return response.text


def parser_html(res_html):

    #print(res_html)

    ret=re.findall('<div class="item">.*?<a href="(.*?)">.*?<span class="title">(.*?)</span>.*?<span class="rating_num".*?>(.*?)</span>.*?<span>(.*?)人评价</span>',res_html,re.S)
    return ret



def store(data):

    with open("douban.txt","a",encoding="utf8") as f:
         for item in data:
             s=" ".join(list(item))
             line=s+"\n"
             print(line)
             f.write(line)

if __name__ == '__main__':

    index=0
    for  i in range(10):

        url="https://movie.douban.com/top250?start=%s&filter="%index

        # 1 爬取资源

        res_html=get_html(url)

        # 2 解析资源

        data=parser_html(res_html)

        # 3 持久化
        store(data)

        index+=25

