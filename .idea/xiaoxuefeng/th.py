#encoding=utf-8
#---------------------------------缩放图片
# from PIL import Image
# import os
# os.chdir('C:\\Users\\Administrator\\Desktop')
# im = Image.open('test.jpg')
# w,h = im.size
# print('Odiginal image size:%sx%s' % (w,h))
# im.thumbnail((w//2,h//2))
# print('Resize image to: %sx%s' %(w//2,h//2))
# im.save('thumbnail.jpg','jpeg')


#-----------------------------图片模糊效果
# from PIL import Image,ImageFilter
import os
os.chdir('C:\\Users\\Administrator\\Desktop')
print(os.path)
with open('text2.txt',encoding='utf8') as f:
    f.read()
#
# im = Image.open('test1.jpg')
# im2=im.filter(ImageFilter.BLUR)
# im2.save('blur.jpg','jpeg')


#--------------------------生成字母验证图片
# from PIL import Image,ImageDraw,ImageFont,ImageFilter
# import random
#
# #生成随机字母
# def rndChar():
#     return chr(random,randint(65,90))
#
# #随机颜色1
# def rndColor():
#     return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#
# #随机颜色2
# def ranColor2():
#     return (random.randint(32,127),random.randint(32,127),random.randint(32.127))
