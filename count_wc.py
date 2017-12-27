#导入正则表达式模块
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 通过wordcloud生成词云
def generate(data):
    words = ''
    for key,values in data.items():
        for i in range(values):
            words += '{}\n'.format(key)
    print(words)
    wc = WordCloud(max_font_size=30, relative_scaling=.5,background_color="white")
    cloud = wc.generate(words)
    plt.imshow(cloud)
    plt.axis("off")
    plt.savefig("res.jpg", dpi=500)


#需统计的英文文本文件名为 test
file_name = 'test.txt'

#行数
lines_count = 0  
#单词总数
words_count = 0  
#字母总数
chars_count = 0  
#单词种类字典
words_dict  = {}   
#行列表
lines_list  = []   

#只读模式打开文件
with open(file_name, 'r') as f:
    for line in f:
        lines_count = lines_count + 1
        chars_count  = chars_count + len(line)
        #搜索line，返回一个list
        match = re.findall(r'[^a-zA-Z]+', line)  
        for i in match:
            # 只要英文单词，删掉其他字符
            line = line.replace(i, ' ')
        #将单词切片以存入列表
        lines_list = line.split()
        #遍历筛选好的单词，获取单词种数
        for i in lines_list:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] = words_dict[i] + 1

#遍历数组，返回键、值
for key,values in words_dict.items():
    print (key,values)
    words_count+=values

generate(words_dict)

print ('单词总数',words_count)
print ('单词种数', len(words_dict))
print ('字母总数', chars_count)
print ('文本行数', lines_count)
