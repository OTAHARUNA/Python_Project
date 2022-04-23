# coding:utf-8
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import pyautogui as pg
import config as cf
from bs4 import BeautifulSoup  # BeautifulSoup をインポート
import csv
# from openpyxl import Workbook


# ブラウザを開く。
driver = webdriver.Chrome(executable_path=cf.CHROMEDRIVER)
driver.get("https://www.ricoh.co.jp/mfp/color/im-C6000-C5500-C4500-C3500-C3000-C2500/spec.html")
content = driver.page_source
BS = BeautifulSoup(content, "html.parser")
# テーブル"wp-block-table is-style-stripes"を指定
table = BS.findAll("table", {"class": "nml nml_scroll"})[0]
rows = table.findAll("tr")  # テーブル中<tr>要素の内容を抽出
print(rows)  # 抽出したHTMLドキュメントを検証
time.sleep(1)

# wb = Workbook()
# mk_name = 'test.xlsx'
# wb.save(mk_name)
# # ワークブックの読み込み
# wb = load_workbook(mk_name)

with open("web-scraping.csv", "w", encoding='utf-8', newline="") as file:  # ファイル名は「web-scraping.csv」を指定する
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):  # tdとth要素をループでファイルに書き込む
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

# ws = wb.active
# ws['A1'] = 'Hello from Python'
# wb.save(mk_name)
