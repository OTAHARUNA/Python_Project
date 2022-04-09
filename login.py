# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui as pg
import config as cf

# ブラウザを開く。
driver = webdriver.Chrome(executable_path=cf.CHROMEDRIVER)
# Googleの検索TOP画面を開く。
driver.get(cf.URL)
driver.maximize_window()
driver.save_screenshot('ログイン画面.png')
time.sleep(3)

# 検証ツールを開く
# pg.typewrite(["F12"])
# time.sleep(3)

# pg.hotkey('ctrl','shift','p')
# driver.send_keys(Keys.CONTROL,"P")
# send_keys(Keys.SHIFT,CONTROL,"P")
# 3秒待機
# time.sleep(3)
# ログインIDを入力
login_email = driver.find_element_by_name("email")
login_email.send_keys(cf.email)
# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys(cf.password)
#ログインボタンをクリック
login_btn = driver.find_element_by_xpath('//*[@class="form-group"]/form/button')
login_btn.click()
time.sleep(3)

# スクール予約確認画面へ遷移
close_btn = driver.find_element_by_xpath('//*[@class="modal-footer"]/button')
close_btn.click()
# スクール予約確認画面へ遷移
reserve_btn = driver.find_element_by_xpath('//*[@id="side-bar"]/ul/li/a')
reserve_btn.click()

driver.maximize_window()
driver.save_screenshot('予約画面.png')

#10秒待機
time.sleep(10)
# ブラウザを終了する。
driver.close()
