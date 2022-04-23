# Python開発の中でのメモ

### できるようになったらよさそうな事
* dockerでLaravel環境構築行い、dawnSNSを改造してログイン機能とかもかえて実装。それを自動化する形で
* エビデンス取得に関して
* Pythonで文字起こし（音声から文字起こし）→副業で文字起こしの作業をこれでいければ
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
### 文字コード
文字コード設定はファイルの頭で行わないとデフォルトのUTF-8になる
```python
# coding:utf-8
```

### 日本語含むファイル名
OpenCVでは日本語含むファイルパスには対応していない。
PILを使用するか、Numpyを使用するかになる。
PILを使用するにしても最終的にはNumpyを使用しているのでNumpyがいいとのこと。

```python
# PIL
import cv2
import numpy as np
from PIL import Image

#とりあえずPILに頼ったらなんとかなるっぽい
img = Image.open('ダウンロード.jpg')
cvimage = np.asarray(img)

# Numpy
import cv2
import numpy as np

img_array = np.fromfile("ダウンロード.jpg", dtype=np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

```
