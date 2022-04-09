from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config as cf

# ドライバー指定でChromeブラウザを開く
browser = webdriver.Chrome(cf.CHROMEDRIVER)

# Googleアクセス
browser.get('https://www.google.com/')

# 検索ボックスを特定
elem = browser.find_element(By.NAME, 'q')
# 「Selenium」と入力して、「Enter」を押す
elem.send_keys('Selenium' + Keys.RETURN)

# ブラウザを閉じる
#browser.quit()
