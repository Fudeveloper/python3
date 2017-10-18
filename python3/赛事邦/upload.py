# -*-coding:utf-8-*-

# 导入webdriver库
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# r表示原始字符
driver = webdriver.Firefox()

# 打开页面
driver.get('file:///C:/Users/Administrator/Desktop/1.html')

btn_upload = driver.find_element_by_id("file")
print btn_upload.get_attribute("name")
btn_upload.click()
import os
time.sleep(1)
os.system(r"1.exe")

driver.save_screenshot("upload.png")
