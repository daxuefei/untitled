#/usr/bin/env python
# _*_ coding:utf-8 _*_
# coding=utf8

#开发者头条的自动登录测试用例

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

try:
    driver.implicitly_wait(10)#反复查找下面的元素，直到10s之后

    # 根据id找到元素，并点击，id和 html 元素的id不同
    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    time.sleep(1)
    driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()
    time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_email")
    ele.send_keys('jcyrss@163.com')
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_password")
    ele.send_keys('sdfsdf')

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id('io.manong.developerdaily:id/btn_login').click()

    #点击发现
    xpath = "//*[@resource-id='io.manong.developerdaily:id/tab_bar']//android.widget.RelativeLayout[4]" \
            "//android.widget.TextView"
    ele = driver.find_element_by_xpath(xpath)
    ele.click()

    time.sleep(1)
    #使用Xpath方式点击我的
    driver.find_element_by_xpath("//*[@resource-id='io.manong.developerdaily:id/tab_bar']"
                                 "//android.widget.RelativeLayout[5]//android.widget.TextView").click()

    #使用tap方式点击我的
    # driver.tap([648, 1135], 300)
    driver_by_elemment_android_u

    pass

except:
    print (traceback.format_exc())


input('**** Press to quit..')
driver.quit()
