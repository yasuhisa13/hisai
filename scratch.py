import time
import openpyxl
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def excel_read():
    cwd = os.getcwd()
    dir = cwd + '/検索パラメータ.xlsx'
    wb = openpyxl.load_workbook(dir)
    ws = wb["Sheet1"]
    # c2は行列番号でA1のセルを取得する
    para = []

    for i in range(1, 50):
        para.append(ws.cell(i, 1).value)
    result = list(filter(None, para))
    return result

'''
for i in excel_read():
    #特定のサイトを開いて検索ボックスにコマンドを入力
    browser = webdriver.Chrome()
    browser.get('https://www.yahoo.co.jp/')
    google_info_link = browser.find_element(By.CLASS_NAME, "_1wsoZ5fswvzAoNYvIJgrU4")

    google_info_link.send_keys(i)
    # Enterキーを押下して検索を実行
    google_info_link.send_keys(Keys.ENTER)
    time.sleep(5)
'''


# 変更前ファイル
path1 = 'C:/Users\yasuh\Downloads/uwsc5302.zip'
path2= 'C:/Users\yasuh\Downloads/hisai.zip'

os.rename(path1, path2)

# ファイルの存在確認
print(os.path.exists(path2))







"""
XPathの取得方法,ボタンクリック
https://web-tweets.com/python/how-to-click-for-python-selenium/#seleniumPython
browser = webdriver.Chrome()
browser.get('https://www.vector.co.jp/download/file/winnt/util/fh688296.html')
google_info_link = browser.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/p[2]/a/img")
google_info_link.click()
time.sleep(5)

"""



# 空白行を削除

