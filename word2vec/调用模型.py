from gensim.models import Word2Vec
import random
#加载模型
model_ = Word2Vec.load("word.model")

#查看相应字向量
# vector= model_.wv['白']
# print(vector)

input_text = '红豆生南国'
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
print(input_text+output_text)