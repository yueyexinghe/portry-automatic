import jieba
import jieba.posseg as pseg

poetry_file ='C:/Users/zhouw/Desktop/python/期末作业/data/data.txt'

n_file = 'C:/Users/zhouw/Desktop/python/期末作业/data/n.txt'
v_file = 'C:/Users/zhouw/Desktop/python/期末作业/data/v.txt'
a_file = 'C:/Users/zhouw/Desktop/python/期末作业/data/a.txt'
o_file = 'C:/Users/zhouw/Desktop/python/期末作业/data/other.txt'

noun=['n','f','s','t','nr','ns','nt','nw','nz']
verb=['v','vd','vn']
adj=['a','ad','an','d']
other=['m','q','r','p','c','u','xc']

content = open(poetry_file).read()
content=content.replace('\n','')
content=content.replace('，','')
content=content.replace('。','')
# print(content)

result_n = open(n_file,'w+',encoding='utf-8')
result_v = open(v_file,'w+',encoding='utf-8')
result_a = open(a_file,'w+',encoding='utf-8')
result_other = open(o_file,'w+',encoding='utf-8')



for word,flag in pseg.cut(content):
        if flag in noun:
            result_n.writelines(word+'\n')
        elif flag in verb:
            result_v.writelines(word+'\n')
        elif flag in adj:
            result_a.writelines(word+'\n')
        else:
            result_other.writelines(word+'\n')


    



