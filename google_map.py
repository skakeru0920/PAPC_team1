from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_route_info(start, dist):
	webdriver_service = Service(ChromeDriverManager().install())
	driver = webdriver.Chrome(service=webdriver_service)

	# 待機時間の設定(10秒でタイムアウト)
	wait = WebDriverWait(driver, 10)

	# Google　Mapにアクセス
	driver.get("https://www.google.co.jp/maps")

	# ルート検索ボタン
	route_button = driver.find_element(By.CSS_SELECTOR, "#hArJGc")
	route_button.click()

	# ルート検索画面が出るまで待機
	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#omnibox-directions > div > div:nth-child(2) > div > div > div > div:nth-child(3) > button')))

	# 公共交通機関を選択
	transport_icon = driver.find_element(By.CSS_SELECTOR, '#omnibox-directions > div > div:nth-child(2) > div > div > div > div:nth-child(3) > button')
	transport_icon.click()


	# 出発地点
	start_input = driver.find_element(By.CSS_SELECTOR, '#sb_ifc50 > input')
	start_input.send_keys(start)

	# 目的地点
	goal_input = driver.find_element(By.CSS_SELECTOR, '#sb_ifc51 > input')
	goal_input.send_keys(dist)

	submit_button = driver.find_element(By.CSS_SELECTOR, '#directions-searchbox-1 > button.mL3xi')
	submit_button.click()

	# ルート情報

	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#section-directions-trip-0 > div.MespJc > div > div.XdKEzd > div')))

	time_ele = driver.find_element(By.CSS_SELECTOR, '#section-directions-trip-0 > div.MespJc > div > div.XdKEzd > div')
	fare_ele = driver.find_element(By.CSS_SELECTOR, '#section-directions-trip-0 > div.MespJc > div > div.ue5qRc > span:nth-child(2)')
	route_info = {"time": time_ele.text, "fare": fare_ele.text}
	driver.quit()
	return route_info
