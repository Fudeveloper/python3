# -*-coding:utf-8-*-

member = "123456"
# 导入webdriver库
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# r表示原始字符
# driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver = webdriver.Firefox()
# 打开页面
driver.get('http://www.cezone.cn/m/login')

username_element, passwd_element = driver.find_elements_by_class_name("form-control")

username_element.send_keys(u"17097351063")
passwd_element.send_keys(u"aabbcc123")

btn_login = driver.find_elements_by_class_name("btn")
btn_login[0].click()
time.sleep(2)

# 保存页面快照
# driver.save_screenshot('1.png')

driver.get('http://www.cezone.cn/m/sign_up/add/8231d6ad85f94b6a8363dba93be73200')
time.sleep(2)




# # 图片上传
import os
btns_img =  driver.find_elements_by_class_name("btn-default")
# print len(btns_img)
# 上传封面
btns_img[0].click()
print btns_img[0].text
time.sleep(2)
os.system(r"1.exe")

time.sleep(2)

# # 参赛作品代表图
# btns_img[2].click()
# os.system(r"1.exe")



# 保存按钮
# driver.find_elements_by_class_name("btn-primary")[0].click()
# driver.save_screenshot('2.png')


# driver.quit()
from selenium.webdriver.support.select import Select

# input 文本框
inputs = driver.find_elements_by_class_name("form-control")
for i in range(len(inputs)):
    if i == 2:
        Select(inputs[i]).select_by_value('43a8414387a542c2aff90be49aee0483')
    elif i == 3:
        inputs[i].send_keys("13960932456")
    elif i in (0,1,4,7, 8, 9, 10):
        inputs[i].send_keys("0000000000000000000000000000000000")
    print i

time.sleep(1)

# 添加成员
btns_img[6].click()
time.sleep(3)

from pymouse import PyMouse
from pykeyboard import PyKeyboard
m = PyMouse()
k = PyKeyboard()

x_dim, y_dim = m.screen_size()
m.click(x_dim/2, y_dim/2, 1)
time.sleep(0.5)
k.press_key(k.tab_key)
k.type_string(member)

k.press_key(k.enter_key)



