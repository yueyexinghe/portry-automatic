import jieba
import jieba.posseg as pseg
import random
from pypinyin import pinyin, lazy_pinyin, Style


n = open('C:/Users/zhouw/Desktop/python/期末作业/data/n.txt','r',encoding='utf-8')
v = open('C:/Users/zhouw/Desktop/python/期末作业/data/v.txt','r',encoding='utf-8')
a = open('C:/Users/zhouw/Desktop/python/期末作业/data/a.txt','r',encoding='utf-8')
o = open('C:/Users/zhouw/Desktop/python/期末作业/data/other.txt','r',encoding='utf-8')


def solve(file):
    list_file = file.readlines()
    for i in range(0, len(list_file)):
        list_file[i] = list_file[i].strip()
    return list_file


def tone_of_word(w):
    s = []
    for i in w:
        #如,u'中'的拼音为 [[u'zho1ng']] ,输出的结果:u'zho1ng'
        pyin = pinyin(i, style=Style.TONE2)[0][0]
        #过滤掉字母，只留数字
        s.append(list(filter(str.isdigit, pyin)))
    return s  #返回数字音调


list_n = solve(n)
list_v = solve(v)
list_a = solve(a)
list_o = solve(o)


noun = ['n', 'f', 's', 't', 'nr', 'ns', 'nt', 'nw', 'nz']
verb = ['v', 'vd', 'vn']
adj = ['a', 'ad', 'an', 'd']
other = ['m', 'q', 'r', 'p', 'c', 'u', 'xc']


input_text = ''
input_text = str(input("请输入上句诗文："))
seg_list = pseg.cut(input_text, use_paddle=True)


def write(seg_list):
    poem = []
    for seg, flag in seg_list:
        flag = str(flag)
        list_final = []

        if (flag in noun):
            try:
                for i in list_n:
                    if tone_of_word(i) == tone_of_word(seg) and seg != i:
                        list_final.append(i)
                poem.append(random.choice(list_final))
            except:
                print("error")
        
        if (flag in verb):
            try:
                for i in list_v:
                    if tone_of_word(i) == tone_of_word(seg) and seg != i:
                        list_final.append(i)
                poem.append(random.choice(list_final))
            except:
                print("error")

        if (flag in adj):
            try:
                for i in list_a:
                    if tone_of_word(i) == tone_of_word(seg) and seg != i:
                        list_final.append(i)
                poem.append(random.choice(list_final))
            except:
                print("error")

        if (flag in other):
            try:
                for i in list_o:
                    if tone_of_word(i) == tone_of_word(seg) and seg != i:
                        list_final.append(i)
                poem.append(random.choice(list_final))
            except:
                print("error")
    return poem


poem = write(seg_list)
output_text = ''
for i in poem:
    output_text = output_text + i
print("原句:" + input_text)
print("续写:" + output_text)
