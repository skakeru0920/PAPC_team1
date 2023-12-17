# やること
# セットアップ（A, B, C, D地点の登録）
# 物件サイトのURLから住所を抽出（スクレイピング）
# 引数として、X地点の住所を取得
# google mapにアクセスし、 AからX地点の経路を検索
# X-A間の情報保存
#   交通手段
#   時間
#   料金
#   乗換回数
#   徒歩→電車→徒歩　などの結果の格納方法　→　トータルの値がわかればOK


import google_map
import config

point_x = '東京都新宿区新宿３丁目３８−１'

for address in config.addresses:
	info = google_map.get_route_info(address[1], point_x)
	print(f'{point_x} から {address[0]} までの所要時間は {info["time"]} 、交通費は {info["fare"]} です。')
	print()
	# print(f'{google_map.get_route_info(address[1], point_x).time} です')
	# print(f'{google_map.get_route_info(address[1], point_x).time} です')
# google_map.get_route_info()
# print(config.addresses[0])

# 仮データ
# print(google_map.get_route_info(point_a, point_x))