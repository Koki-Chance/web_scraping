from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd
import os
import datetime

USER = "test_user"
PASS = "test_pw"

# GoogleChromeを起動
browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(3)

# 対象ページにアクセス
url_login = "https://kino-code.com/membership-login"
browser.get(url_login)
# time.sleep(2)
print("ログインページにアクセスしました\n")

# ログイン
print("ログインを開始します\n")
element = browser.find_element_by_id('swpm_user_name')
element.clear()
element.send_keys(USER)
element = browser.find_element_by_id('swpm_password')
element.clear()
element.send_keys(PASS)
print("フォーム送信開始")

# ログインボタンクリック 
browser_form = browser.find_element_by_name('swpm-login')
# time.sleep(1)
browser_form.click()
print("ユーザー情報入力完了、ログインボタンをクリックしました。")
print("ログインを完了しました")


# ファイルのダウンロード(ページへアクセス)
url = "https://kino-code.com/member-only/"
# time.sleep(1)
browser.get(url)
# time.sleep(2)
print(url, ":アクセス完了")

# ファイルのダウンロード(ダウンロード)
frm = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div/main/article/div/p[2]/button')
# time.sleep(1)
frm.click()
print("ダウンロードを完了しました")


