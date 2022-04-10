# Python開発の中でのメモ
## ライブラリSelenium利用

```python
#ショートカットキー
import pyautogui as pg

pg.typewrite(["F12"])
pg.hotkey('ctrl','shift','p')
```
### 文字列と数値を結合する事はできない。数値を文字列型に変換してから

```python
xpath = '//*[@id="side-bar"]/ul/li[' + str(no) + ']/a'
```

### Pythonでの繰り返し文の書き方
```python
for no in range(3): #0,1,2
for no in range(1,4): #1,2,3
    range(4,7) # 4 5 6
    range(0, 10, 2) #0 2 4 6 8
#特に終わりの宣言は不要でforの中身はインデント下げて、抜け出すときはインデント同じ
```

```python
for no in range(1,4):
    xpath = '//*[@id="side-bar"]/ul/li[' + str(no) + ']/a'
    reserve_btn = driver.find_element_by_xpath(xpath)
    reserve_btn.click()

    driver.maximize_window()
    driver.save_screenshot('./images_evidence/予約画面' + str(no) + '.png')
#特に終わりの宣言は不要でforの中身はインデント下げて、抜け出すときはインデント同じ
```
