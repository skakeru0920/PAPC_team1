# webスクレイピングのサンプルプログラム(その1)
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

# 終わっても閉じないように
options = Options()
options.add_experimental_option('detach', True)

# ChromeDriverManagerの読み込み
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service, options=options)


# 待機時間の設定(10秒でタイムアウト)
wait = WebDriverWait(driver, 10)

# Google　Mapにアクセス
driver.get("https://www.google.co.jp/maps")


# CSSセレクターで検索テキストを指定し入力して検索する
route_button = driver.find_element(By.CSS_SELECTOR, "#hArJGc")
# route_button.send_keys('ChatGPT')
route_button.click()

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#omnibox-directions > div > div:nth-child(2) > div > div > div > div:nth-child(3) > button')))

transport_icon = driver.find_element(By.CSS_SELECTOR, '#omnibox-directions > div > div:nth-child(2) > div > div > div > div:nth-child(3) > button')
transport_icon.click()

# 仮データ
point_x = '東京都新宿区新宿３丁目３８−１'
point_a = '東京都千代田区丸の内１丁目'

start_input = driver.find_element(By.CSS_SELECTOR, '#sb_ifc50 > input')
start_input.send_keys(point_x)

goal_input = driver.find_element(By.CSS_SELECTOR, '#sb_ifc51 > input')
goal_input.send_keys(point_a)

submit_button = driver.find_element(By.CSS_SELECTOR, '#directions-searchbox-1 > button.mL3xi')
submit_button.click()

# ルート情報

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#section-directions-trip-0 > div.MespJc > div > div.XdKEzd > div')))

time_ele = driver.find_element(By.CSS_SELECTOR, '#section-directions-trip-0 > div.MespJc > div > div.XdKEzd > div')
fare_ele = driver.find_element(By.CSS_SELECTOR, '#section-directions-trip-0 > div.MespJc > div > div.ue5qRc > span:nth-child(2)')
route_info = {"time": time_ele.text, "fare": fare_ele.text}
print(route_info)

# # トップページのニュースの情報を取得
# html = driver.page_source

# soup = BeautifulSoup(html, 'html.parser')

# # pickupがトップページのニュースになるのでその要素だけを抽出
# elements = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))

# # 取得した情報をファイルに書き出す
# file_path = "yahoo_news.txt"
# file = open(file_path, 'a')

# for data in elements:
#     # f-stringsを使うことでコードを短くできる
#     file.write(f"{data.span.string}\n")
#     file.write(f"{data.attrs['href']}\n")

driver.quit()