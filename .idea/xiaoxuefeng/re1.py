#re
# import re
# re.match(r'^\d{3}\-\d{3,8}$', '010-12345')

#match()判断是否匹配
# import re
# test = '用户输入字符串'
# if re.match(r'正则表达式',test):
#     print(ok)
# else:
#     print('failed')


#切分字符串
# import re
# r=re.split(r'\s+','a b      c')
# print(r)

#普通的切分字符串无法处理多个空格的情况
# r='a b     c'.split(' ')
# print(r)

#---------------------分组
# import re
# m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
# print(m)
# print(m.group(0))
# print(m.group(1))


#-------贪婪匹配
import re
r=re.match(r'^(\d+?)(0*)$','102300')
print(r.group())
print(r.group(2))
print(r.group(1))


















