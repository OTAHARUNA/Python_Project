# coding:utf-8
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config as cf
from bs4 import BeautifulSoup  # BeautifulSoup をインポート
from openpyxl import Workbook
import subprocess


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

wb = Workbook()
mk_name = 'test.xlsx'
wb.save(mk_name)
# ワークブックの読み込み
wb = load_workbook(mk_name)
ws = wb.active
row_count = 0
for row in rows:
    csvRow = []
    row_count = row_count + 1
    for cell in row.findAll(['td', 'th']):  # tdとth要素をループでファイルに書き込む
        csvRow.append(cell.get_text())
    if csvRow[0] == "\xa0" :
        # del csvRow[0]
        csvRow[0] == ""
    # writer.writerow(csvRow)
    for idx in range(1,len(csvRow)+1):
        ws.cell(row=row_count, column=idx, value=csvRow[idx-1])
ws.column_dimensions['A'].width = 34
ws.column_dimensions['B'].width = 34
ws.column_dimensions['C'].width = 34
ws.column_dimensions['D'].width = 34
wb.save(mk_name)
EXCEL = r'C:\Users\chopp\Project\Python_Project\test.xlsx'
subprocess.Popen(['start', EXCEL], shell=True)
time.sleep(10)
