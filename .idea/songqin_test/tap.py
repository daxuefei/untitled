#/usr/bin/env python
# _*_ coding:utf-8 _*_
# coding=utf8

from appium import webdriver
import time,traceback



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'test'#连接多个设备才有用
# desired_caps['app'] = r'e:\apk\toutiao.apk'#如果已经安装好软件乐意不需要，这边填写的是apk在电脑上的路径
desired_caps['appPackage'] = 'io.manong.developerdaily'#app的包名，唯一标志app
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'#对应安卓应用的操作界面
desired_caps['unicodeKeyboard']  = True#安装一个中文的输入法
desired_caps['resetKeyboard']  = True#
desired_caps['noReset'] = True#清除元素数据，跳过初始页面
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#把上述参数传给appium services

#等待界面出现
driver.find_element_by_class_name("android.widget.ImageButton")

#使用tap的方式点击我的按钮
driver.tap([625,1112],[671,1158],300)





input('**** Press to quit..')
driver.quit()