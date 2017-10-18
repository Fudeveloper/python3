# -*-coding:utf-8-*-
from selenium import webdriver

driver = webdriver.Firefox()

# 打开页面
driver.get('file:///C:/Users/Administrator/Desktop/3.html')
driver.find_element_by_id("confirm").click()
import time
time.sleep(2)
driver.switch_to.alert.accept()