# -*-coding:utf-8-*-
import phone
import random
import time
import os
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from selenium import webdriver

m = PyMouse()
k = PyKeyboard()
# -----------------------C:\Users\Administrator\Desktop\img\22-0.jpg
# C:\Users\Administrator\Desktop\img\22-1.jpg
# ------------------------- 配置部分 ------------------------------------------------
# 固定密码C:\Users\Administrator\Desktop\img\193-0.jpg

passwd = "aabbcc123"
# 当前索引
now_index = 0

# 账号
phone_number = phone.get_phone_by_index(now_index)

# 封面图片路径
img1 = r"C:\Users\Administrator\Desktop\img\{0}-0.jpg".format(now_index)
# 代表图路径
img2 = r"C:\Users\Administrator\Desktop\img\{0}-1.jpg".format(now_index)
import teacher_info

random_index = random.choice(range(15))
teacher = teacher_info.get_teacher_by_index(random_index)
# 作品名称
import return_title

product_name = return_title.get_title_by_index(now_index)
# 指导老师
teacher_name = teacher['name']
# 导师电话
teacher_phone = teacher['phone']
# 团队成员账号
member_username = ""
# 设计创意说明
idea_start_index = now_index * 50
import return_idea

idea = return_idea.get_content_by_start(idea_start_index)
# 项目摘要
import return_summary

summary = return_summary.get_summary_by_start_index(idea_start_index)
# 市场分析与营销策略
import return_analysis

analysis = return_analysis.get_finance_by_start_index(idea_start_index)
# 投资、财务、风险分析与对策
import return_finance

finance = return_finance.get_analysis_by_start_index(idea_start_index)
# 团组成与企业愿景
import return_vision

vision = return_vision.get_vision_by_start_index(idea_start_index)
# ------------------------------------------------ 运行部分 ------------------------------------------------


driver = webdriver.Firefox()

# 打开页面
driver.get('http://www.cezone.cn/m/login')

# 填写账号密码
username_element, passwd_element = driver.find_elements_by_class_name("form-control")
username_element.send_keys(phone_number)
passwd_element.send_keys(passwd)

# 登陆
btn_login = driver.find_elements_by_class_name("btn")
btn_login[0].click()
time.sleep(1)

# 打开报名页面
driver.get('http://www.cezone.cn/m/sign_up/add/8231d6ad85f94b6a8363dba93be73200')
time.sleep(2)
btns_img = driver.find_elements_by_class_name("btn-default")

# ------------------------------------------------ 上传图片部分 ------------------------------------------------
# 上传封面
btns_img[0].click()
time.sleep(1.5)
k.type_string(img1)
time.sleep(1.5)
k.press_key(k.enter_key)
time.sleep(1)

# 上传参赛作品代表图
btns_img[2].click()
time.sleep(1.5)
k.type_string(img2)
time.sleep(1.5)
k.press_key(k.enter_key)
time.sleep(1.5)

# ------------------------------------------------ 信息填写 ------------------------------------------------
from selenium.webdriver.support.select import Select

# input 元素树
inputs = driver.find_elements_by_class_name("form-control")
# 填写作品名称
inputs[0].send_keys(product_name.decode('utf-8'))
# 填写指导老师
inputs[1].send_keys(teacher_name.decode('utf-8'))
# 填写赛事分类
Select(inputs[2]).select_by_value('43a8414387a542c2aff90be49aee0483')

# 填写导师电话
inputs[3].send_keys(teacher_phone.decode('utf-8'))

# 填写设计创意说明
inputs[4].send_keys(idea.decode('utf-8'))
# 填写项目摘要
inputs[7].send_keys(summary.decode('utf-8'))
# 填写市场分析与营销策略
inputs[8].send_keys(analysis.decode('utf-8'))
# 填写投资、财务、风险分析与对策
inputs[9].send_keys(finance.decode('utf-8'))
# 填写团组成与企业愿景
inputs[10].send_keys(vision.decode('utf-8'))

# ------------------------------------------------ 添加成员 ------------------------------------------------
# btns_img[6].click()
# time.sleep(2)
#
# x_dim, y_dim = m.screen_size()
# m.click(x_dim / 2, y_dim / 2, 1)
# time.sleep(0.5)
# k.press_key(k.tab_key)
# k.type_string(member_username)
# k.press_key(k.enter_key)
#
# time.sleep(3)
# ------------------------------------------------ 提交 ------------------------------------------------
driver.find_element_by_id("release-btn").click()
time.sleep(2)
for i in range(10):
    m.click(808 - 200 + 50, 585 - 110, 1)
with open('complete.txt', 'a') as f:
    f.write(str(now_index) + '----' + phone_number + '\n')
