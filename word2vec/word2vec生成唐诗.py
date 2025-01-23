from gensim.models import Word2Vec
import pandas as pd
import numpy as np
import random

'''
model=Word2Vec(sentences,sg=1,size=100,window=5,min_count=5,negative=3,sample=0.001,hs=1,workers=4)
参数配置详情：
（1）sentences 第一个参数是预处理后的训练语料库，是可迭代列表，但是对于较大的语料库，可以直接从磁盘/网络传输句子迭代。
（2）sg=1是skip-gram算法，对于低频词敏感；默认sg=0为CBOW算法
（3）size(int) 是输出词向量的维数默认值是100,。这个维度的取值和我们的语料库大小有关，比如小于100M的文本语料库，则使用默认值就可以。如果是超大语料库，建议增大维度。值太小会导致词映射因为冲突而导致影响结果，值太大则会耗内存并使计算变慢，一般取值为100到200之间，不过见的比较多的也有300的维度
（4）window(int) 是一个句子中当前单词和预测单词之间的最大距离，window越大，则和某一较远的词也会产生上下文关系。默认值为5。window值越大所需要枚举的预测词越多，计算时间越长。
（5）min_count 忽略所有频率低于此值的但单词，默认值是5.
（6）workers表示训练词向量时使用的进程数，默认是但当前运行机器的处理器核数。
还有关于采样和学习率的，一般不常设置:
（1）negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值是 1e-3。
（2）hs=1 表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被使用。
'''

file_five= open('C:/Users/zhouw/Desktop/python/人工智能实践/期末作业/data/五言律诗.txt','r')
list_five=file_five.readlines()
# print(list_five)
for i in range(0,len(list_five)):
    list_five[i]=list_five[i].strip()
    list_five[i]=list_five[i][0:5]+list_five[i][6:11]
    # print(list_five[i])

array_ = np.array(list_five).reshape(683,)#转化为一维矩阵
# print(array_)

model_dis = Word2Vec(array_,sg=1,window=20,min_count=1,negative=10,ns_exponent=-0.8)
#保存模型
model_dis.save('word.model')

#加载模型
model_ = Word2Vec.load("word.model")

#查看相应字向量
# vector= model_.wv['白']
# print(vector)

input_text = '床前明月光'
output_text=''



for token in input_text:
        print(token)
        if token in model_.wv.index_to_key:
            max_similarity=-1
            for match_token in model_.wv.most_similar(positive=[token]):
                if match_token[1] > max_similarity:
                    max_similarity = match_token[1]
                    best_match = match_token[0]
                    # print(best_match)
                    output_text = output_text+str(random.choice([x[0] for x in model_.wv.most_similar(positive=[best_match])]))
                    print(model_.wv.most_similar(positive=[best_match]))
print("原句:"+input_text)
print("续写:"+output_text)