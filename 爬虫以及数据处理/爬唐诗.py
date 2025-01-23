import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

file = open('C:/Users/zhouw/Desktop/python/期末作业/data/data.txt', "w")

# 使用beautifulsoup爬取唐诗三百首
url1='https://so.gushiwen.cn/gushi/tangshi.aspx'
text=requests.get(url=url1).text
soup=BeautifulSoup(text,'lxml')
div=soup.find_all('div',{'class':'left'})[1]
spans=div.find_all('span')
for span in spans:
    a=span.find('a')
    # 尝试寻找链接(可能存在a链接不存在的可能性)
    try:
        a=str(a).split('"')
        # print(a[1])
        # 链接链入诗中
        url='https://so.gushiwen.cn{}'.format(a[1])
        text=requests.get(url=url).text
        # 使用xpath爬取网页
        tree=etree.HTML(text)
        # 网页里面xpath存在两种情况，使用try来写(注意两者先后不能错)
        try:
            datas=tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/p/text()')
            if(datas==[]):
                # 这里是如果第一种方法获取到的list为空，则主动抛出一个异常
                raise ImportError
        except:
            datas=tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/text()')

        for data in datas:
            # 使用strip去除头尾的\n
            data=data.strip()
            # 使用正则表达式去除()
            data=re.sub(u"\\(.*?\\)", "", data)
            file.write(str(data)+'\n')
            # print(data)

    except:
        print("不存在")
        continue
# sons=div.find_all('div',class_="span")
# print(sons)


# for i in div:
#     print(i)
#     print('aaaaaaaaaaaaaaaa')
