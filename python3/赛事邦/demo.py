# -*-coding:utf-8-*-
import phone
import random
import time
import os
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
# ------------------------------------------------ 配置部分 ------------------------------------------------
# 固定密码
passwd = "aabbcc123"

# 当前索引
now_index = 2

# 账号
phone_number = phone.get_phone_by_index(now_index)

# 封面图片路径
img1 = r"C:\Users\Administrator\Desktop\{0}-1.png".format(now_index)
# 代表图路径
img2 = r"C:\Users\Administrator\Desktop\{0}-2.png".format(now_index)
import teacher_info

random_index = random.choice(range(15))
teacher = teacher_info.get_teacher_by_index(random_index)
# 作品名称
product_name = "餐厅商业计划书"
# 指导老师
teacher_name = teacher['name']
# 导师电话
teacher_phone = teacher['phone']
# 团队成员账号
member_username = phone.get_phone_by_index(200 - now_index)
# 设计创意说明
idea = "宗旨， 以“真诚办事， 寻求杰出;创造康健，共同分享”为任务，实行差异化战略和品牌战略，打造 DIY 特色品牌， 办事一流特色品牌， 环境优雅特色品牌， 餐厅范围大品牌， 康健宁静饮食品牌。"
# 项目摘要
summary = "长期生长战略， 具体战略如下： ? 初期战略(1-2 年) 初期的策划战略紧张是创建主顾干系，与食风致料商家创建业务干系，在主顾口中打出良好 的口碑; 紧张的市场战略为先开辟目的市场的重点或紧张主顾， 在主顾心目中创建本身的品牌形象，积累无形资产，可以大概收回初期投资并赢利;同时准备扩大餐厅策划范围，开辟更多的潜在客 户，提高市场份额。"
# 市场分析与营销策略
analysis = "餐饮业是全中国第三产业中一个非常紧张的支柱， 中国人有一句俗话： 民以食为天。 据相识， 中高收入国家平均每 268 人就拥有一家餐馆，而在我国约 2000 人才拥有一家餐馆。这一数字表 明，中国的餐饮市场远远没有饱和，潜力很大，巨大的商机在等着我们去施展本身的聪明本领， 甜睡的金山等候着我们去发掘。"
# 投资、财务、风险分析与对策
finance = "餐厅在初期的策划战略紧张是创建主顾干系，与食风致料商家创建业务干系，在主顾口中打 出良好的口碑; 紧张的市场战略为先开辟目的市场的重点或紧张主顾， 在主顾心目中创建本身的 品牌形象，积累无形资产，可以大概收回初期投资并赢利;同时准备扩大餐厅策划范围，开辟更多的 潜在客户，提高市场份额。 第一年紧张任务： (1)开心开辟市场，依据消耗者要求，扩大业务范畴;真诚办本家儿顾，提高餐厅质量，树 立品牌形象; (2)餐厅的消耗议决宣传事情举行投放; (3)在仙林大学城创建营销渠道网; (4)与食物质料方创建业务条约干系，包管餐厅的连续供货渠道. "
# 团组成与企业愿景
vision = "随着社会的生长，人们的生存在物质方面得到餍足后，便开始寻求精神层面的享受。而人对 精神层面的需求排在最顶尖的便是自我实现的需求。这也是近几年来 DIY(Do it yourself,“亲 历亲为”，本身去做，本身段验，挑衅自我，享受此中快乐的一种精神)鼓起的缘故原由。而做饭， 可以说是传统的 DIY。大部门人都市做饭，至少也会做一两个菜(这也是这个项目可以实施的一 个须要条件)。"
# ------------------------------------------------ 运行部分 ------------------------------------------------
from selenium import webdriver

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
time.sleep(2)
k.type_string(img1)
time.sleep(1)
k.press_key(k.enter_key)
time.sleep(1)

# 上传参赛作品代表图
btns_img[2].click()
time.sleep(1)
k.type_string(img1)
time.sleep(1)
k.press_key(k.enter_key)
time.sleep(1)


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
btns_img[6].click()
time.sleep(2)

x_dim, y_dim = m.screen_size()
m.click(x_dim / 2, y_dim / 2, 1)
time.sleep(0.5)
k.press_key(k.tab_key)
k.type_string(member_username)
k.press_key(k.enter_key)

time.sleep(3)
# ------------------------------------------------ 提交 ------------------------------------------------
# driver.find_element_by_id("release-btn").click()
# time.sleep(3)
# for i in range(10):
#     m.click(808 - 200 + 50, 585 - 110, 1)
