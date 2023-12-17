import re
import google_map
import config
import get_address


# https://suumo.jp/chintai/tokyo/city/
# このサイトから住みたい物件の条件を指定して検索したURLを base_url に入力する

# 2件hitのurlサンプル
# base_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=30&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&rn=0005&ek=000520110&ra=013&cb=8.5&ct=9.0&md=02&et=5&mb=0&mt=9999999&cn=9999999&fw2="

base_url = input("SUUMOの検索結果URLを入力してください: ")

print()
#物件情報が保存される配列 (駅名, 駅徒歩)
property_info = get_address.get_address(base_url)

for i in range(len(property_info[0])):
	#物件名
	point_x = property_info[0][i]

	# 最寄り駅
	station = property_info[1][i]

	#駅徒歩時間
	walk_time = property_info[2][i]

	print(f'\033[92m\033[1m# {point_x} (最寄り駅: {station}から徒歩{walk_time}分) までの経路情報 ↓\033[0m')
	for address in config.addresses:
		info = google_map.get_route_info(address[1], station)
		sum_time = walk_time + int(re.sub(r"\D", "", info["time"]))
		print(f'  - {address[0]} までの所要時間は {sum_time} 分、交通費は {info["fare"]} です。')
	print("\n")