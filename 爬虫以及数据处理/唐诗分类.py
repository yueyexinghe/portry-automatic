file = open('C:/Users/zhouw/Desktop/python/期末作业/data/data.txt')
file1= open('C:/Users/zhouw/Desktop/python/期末作业/data/五言律诗.txt','w')
file2= open('C:/Users/zhouw/Desktop/python/期末作业/data/七言律诗.txt','w')
# f5=open('./test.txt', encoding='utf-8')
contents=file.readlines()
file.close()
for i in range(0,len(contents)):
    contents[i]=contents[i].strip()
    # print(len(contents[i]))
    if len(contents[i])==12:
        file1.write(str(contents[i])+'\n')
    elif len(contents[i])==16:
        file2.write(str(contents[i])+'\n')
