#-*- encoding:utf-8 -*-
# import string
#
# path='C:/Users/Administrator/Desktop/Walden.txt'
#
# with open(path,'r',encoding = 'UTF-8') as text:
#     words=[raw_word.lstrip(string.punctuation).lower() for raw_word in text.read().split()]#
#     words_index=set(words)
#     counts_dict = {index:words.count(index) for index in words_index}#创建一个以单词为key，出现的频率为value的字典
#
#
# for word in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):#已字典中的值为排序的参数
#     print('{} -- {} times'.format(word,counts_dict[word]))


name='xiaohua'

def eat():
    print(f'{name}改吃饭了')
eat()


