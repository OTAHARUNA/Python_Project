# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import config as cf

# ブラウザを開く。
driver = webdriver.Chrome(executable_path=cf.CHROMEDRIVER)
# Googleの検索TOP画面を開く。
driver.get(cf.URL)
# 検証ツールを開く
pyautogui.typewrite(["F12"])
# 3秒待機
time.sleep(3)
# ログインIDを入力
login_email = driver.find_element_by_name("email")
login_email.send_keys(cf.email)
# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys(cf.password)
#ログインボタンをクリック
login_btn = driver.find_element_by_xpath('//*[@class="form-group"]/form/button')
login_btn.click()
#10秒待機
time.sleep(10)
# ブラウザを終了する。
driver.close()
