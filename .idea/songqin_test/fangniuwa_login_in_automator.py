#/usr/bin/env python
# _*_ coding:utf-8 _*_

# /usr/bin/env python
# _*_ coding:utf-8 _*_
# coding=utf8


#放牛娃appandroid版 的自动登录测试用例

from appium import webdriver
import time,traceback
import os




desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'test'#连接多个设备才有用
# desired_caps['app'] = r'e:\apk\toutiao.apk'#如果已经安装好软件乐意不需要，这边填写的是apk在电脑上的路径
desired_caps['appPackage'] = 'com.xiniunet.xntalk'#app的包名，唯一标志app
desired_caps['appActivity'] = 'com.xiniunet.xntalk.common.activity.splash.SplashActivity'#对应安卓应用的操作界面
desired_caps['unicodeKeyboard']  = True#安装一个中文的输入法
desired_caps['resetKeyboard']  = True#
desired_caps['noReset'] = True#清除元素数据，跳过初始页面
desired_caps['newCommandTimeout'] = 6000
#启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#把上述参数传给appium services

try:
    driver.implicitly_wait(10)#反复查找下面的元素，直到10s之后

    # # 根据id找到元素，并点击，id和 html 元素的id不同
    # driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()
    # time.sleep(1)
    # driver.find_element_by_id("io.manong.developerdaily:id/btn_email").click()
    # time.sleep(1)

    # 输入用户名、密码
    ele = driver.find_element_by_id("com.xiniunet.xntalk:id/et_account")
    ele.send_keys('15370135956')
    ele = driver.find_element_by_id("com.xiniunet.xntalk:id/et_password")
    ele.send_keys('123456')

    time.sleep(2)
    # 点击登录
    driver.find_element_by_id('com.xiniunet.xntalk:id/btn_login').click()

    #点击发现
    # xpath = "//*[@resource-id='android:id/tabhost']//android.widget.FrameLayout[5]" \
    #         "//android.widget.TextView"
    # ele = driver.find_element_by_xpath(xpath)
    # ele.click()
    # driver.find_element_by_android_uiautomator("text(\"发现\")").click()
    # time.sleep(3)
    # driver.find_element_by_android_uiautomator('text(\"社区\")').click()
    # time.sleep(3)
    # driver.find_element_by_android_uiautomator('new UiSelector().className("android.view.View").childSelector(new UiSelector().index("3")').click()
    # time.sleep(3)
    # driver.find_element_by_android_uiautomator(
    #     'new UiSelector().resourceId("android:id/content").childSelector(new UiSelector().className("android.view.View")[3]))').click()

    # driver.swipe(1000,150).click()
    # time.sleep(1)
    # #使用Xpath方式点击我的
    # driver.find_element_by_xpath("//*[@resource-id='android:id/tabs']//android.widget.FrameLayout[3]//android.widget.TextView").click()#ok
    # # sleep(3)
    # # driver.find_element_by_id('com.xiniunet.xntalk:id/rl_buddy_scanner').cliack()
    # time.sleep(2)
    # # driver.find_element_by_android_uitomator('new UISelector().text("我")').click()#不能实现点击操作
    # # driver.find_elememnt_by_id('com.xiniunet.xntalk:id/rl_buddy_scanner').cliack()#点击进入我的开票公司
    # driver.find_elememt_by_xpath("//*[@resource-id='com.xiniunet.xntalk:id/gv_applications_common']//android.widget.LinearLayout[0]//android.widget.TextView").click()

    # driver.find_element_by_android_uiautomator("text(\"放牛娃\")").click()
    # time.sleep(3)
    # driver.find_element_by_android_uiautomator('text(\"审批中心\")').click()
    # time.sleep(3)
    # driver.find_element_by_android_uiautomator('text(\"我提交的\")').click()
    # time.sleep(2)
    # #点击搜索输入框
    # ele=driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText")')
    # ele.click()
    #输入需要搜索的信息并点击搜索
    # ele.send_keys('管理员')
    # driver.keyevent(66)
    # driver.press_keycode(66)
    # time.sleep(3)
    # driver.find_element_by_android_uiautomator('new UiSelector().className("android.view.ViewGroup")').click()

    #使用tap方式点击我的
    # driver.tap([648, 1135], 300)





    #--------------发帖
    driver.implicitly_wait(50)
    driver.find_element_by_android_uiautomator('new UiSelector().text(\"发现\")').click()
    driver.implicitly_wait(50)
    driver.find_element_by_id('com.xiniunet.xntalk:id/rl_forum_sp').click()
    driver.implicitly_wait(50)
    xpath ="//*[@resource-id='android:id/content']//android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView"
    driver.find_element_by_xpath(xpath).click()

    driver.implicitly_wait(50)
    driver.find_element_by_android_uiautomator('new UiSelector().text(\"发帖\")').click()
    driver.implicitly_wait(50)
    title = driver.find_element_by_android_uiautomator('new UiSelector().text(\"标题（必填），4-40字\")')
    title.click()
    title.send_keys('自动发帖啦！')
    time.sleep(1)
    con = driver.find_element_by_android_uiautomator('new UiSelector().text(\"正文，来吧，尽情发挥吧...\")')
    con.send_keys('猜猜我想说啥？哈哈')
    driver.implicitly_wait(50)
    driver.find_element_by_android_uiautomator('new UiSelector().text(\"发表到板块\")').click()
    driver.implicitly_wait(50)
    # idOrXpath = "//*[@resource-id='android:id/content']//android.widget.ScrollView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView"
    # def find_element(driver,idOrXpath,n=10):
    #     for i in xrange(n):
    #         try:
    #             if idOrXpath.startswith('/'):
    #                 ret = driver.find_element_by_xpath(idOrXpath)
    #             else:
    #                 ret =driver.find_element_by_id(idOrXpath)
    #             return ret
    #         except Exception as err:
    #             print(err.message)
    #             time.sleep(2)
    #     raise Exception('element %s could not be foud' %idOrXpath)

    # idOrXpath= "//*[@resource-id='android:id/content']//android.view.View[1]/android.view.View/android.view.View[2]/android.widget.ScrollView/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.TextView"

    # driver.find_element_by_xpath(idOrXpath).click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text(\"放牛娃\")').click()




    driver.implicitly_wait(50)
    driver.find_element_by_android_uiautomator('new UiSelector().text(\"提交\")').click()
    time.sleep(20)

    pass

except:
    print (traceback.format_exc())


input('**** Press to quit..')
driver.quit()