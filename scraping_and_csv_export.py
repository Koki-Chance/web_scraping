from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd
import pprint
pp = pprint.PrettyPrinter(indent=1)

url = "https://kino-code.com/python-scraping/"
response = req.urlopen(url)

parse_html = BeautifulSoup(response, 'html.parser')

# htmlを整形(インデント)し、見やすくする
# print(parse_html.prettify)

# タイトルを取得（titleタグを除く）
# print(parse_html.title.string)

# aタグ要素を全て取得し、title_listsに代入
title_lists = parse_html.find_all('a')

# title_listsの中から、最初の１０個の要素を表示する
# print(title_lists[10].string)

# title_listsのうち、はじめの１０個のurlを取得し、表示する
# print(title_lists[10].attrs['href'])

# 取得した全てのurlをtitle_listに代入する
title_list=[]
url_list=[]

# title_lists からタイトルとURLを取り出し、配列(title_list, url_list)に代入
for i in title_lists:
  title_list.append(i.string)
  url_list.append(i.attrs['href'])

# title_list と url_list の中身を表示する
print('\ntitle: ')
pp.pprint(title_list)
print('\nURL: ')
pp.pprint(url_list)

# 取得したtitleと
df_title_url = pd.DataFrame({'Title': title_list, 'URL': url_list})
# print(df_title_url)

# Noneが存在するレコードを削除
df_notnull = df_title_url.dropna(how='any')
# print(df_notnull)

# 特定の文字に一致するレコードのみを保持する
# print(df_notnull['Title'].str.contains('Python超入門コース'))
# str.endswith: 特定の文字列で終わるか判定/str.startswith: 特定の文字列で始まるか判定
pp.pprint(df_notnull[df_notnull['Title'].str.contains('Python超入門コース')])

df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]

# df_contain_python(必要レコードのみを抽出したデータフレーム)をcsvにエクスポート
df_contain_python.to_csv('../output.csv')