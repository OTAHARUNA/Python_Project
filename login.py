# coding:utf-8
from selenium import webdriver
import time
import config as cf

# ブラウザを開く。
driver = webdriver.Chrome(executable_path=cf.CHROMEDRIVER)
# Googleの検索TOP画面を開く。
driver.get(cf.URL)
driver.maximize_window()
driver.save_screenshot('./images_evidence/login.png')
time.sleep(1)

# ログインIDを入力
login_email = driver.find_element_by_name("email")
login_email.send_keys(cf.email)
time.sleep(1)
# パスワードを入力
password = driver.find_element_by_name("password")
password.send_keys(cf.password)
time.sleep(1)

#ログインボタンをクリック
login_btn = driver.find_element_by_xpath('//*[@class="form-group"]/form/button')
login_btn.click()
time.sleep(1)

# 閉じるボタン押下
close_btn = driver.find_element_by_xpath('//*[@class="modal-footer"]/button')
close_btn.click()

# スクール予約確認画面へ遷移
for no in range(1,4):
    xpath = '//*[@id="side-bar"]/ul/li[' + str(no) + ']/a'
    reserve_btn = driver.find_element_by_xpath(xpath)
    reserve_btn.click()

    driver.maximize_window()
    driver.save_screenshot('./images_evidence/yoyaku' + str(no) + '.png')

#10秒待機
time.sleep(5)
# ブラウザを終了する。
driver.close()
