from pypinyin import pinyin, lazy_pinyin, Style


n = open('C:/Users/zhouw/Desktop/python/期末作业/data/n.txt','r',encoding='utf-8')
def solve(file):
    list_file=file.readlines()
    for i in range(0,len(list_file)):
        list_file[i]=list_file[i].strip()
    return list_file

list_n=solve(n)

def tone_of_word(w):
    s=[]
    
    for i in w:
        #如,u'中'的拼音为 [[u'zho1ng']] ,输出的结果:u'zho1ng'
        pyin=pinyin(i, style=Style.TONE2)[0][0]
        #过滤掉字母，只留数字
        s.append(list(filter(str.isdigit, pyin)))
    return s #返回数字音调

result = tone_of_word('入海流')
print(result)
for i in list_n:
    result1=tone_of_word(i)
    if(result1==result):
        print(i)


