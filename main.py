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


import re
import google_map
import config
import	get_address


# https://suumo.jp/chintai/tokyo/city/
# このサイトから住みたい物件の条件を指定して検索したURLを base_url に入力する
# base_url = input("SUUMOの検索結果URLを入力してください: ")

# 2件hit
base_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&pc=30&smk=&po1=25&po2=99&shkr1=03&shkr2=03&shkr3=03&shkr4=03&rn=0005&ek=000520110&ra=013&cb=8.5&ct=9.0&md=02&et=5&mb=0&mt=9999999&cn=9999999&fw2="

#物件情報が保存される配列 (駅名, 駅徒歩)
property_info = get_address.get_address(base_url)


# roop処理
# roopの中では、各情報にアクセスできる(物件名、最寄り駅、駅徒歩、家賃、階数、URLなど)
# point_x = '東京都新宿区新宿３丁目３８−１'
# # 物件名
# point_x = property_info[0][0]

# # 最寄り駅
# station = property_info[1][0]

# # 駅徒歩時間
# walk_time = property_info[2][0]

# 物件ごとのloop
for i in range(len(property_info[0])):
	#物件名
	point_x = property_info[0][i]

	# 最寄り駅
	station = property_info[1][i]

	#駅徒歩時間
	walk_time = property_info[2][i]

	print(f'# {point_x} の情報について（最寄り駅:{station}駅から徒歩{walk_time}分) ↓')
	for address in config.addresses:
		info = google_map.get_route_info(address[1], point_x)
		sum_time = walk_time + int(re.sub(r"\D", "", info["time"]))
		print(f'  -{address[0]} までの所要時間は {sum_time} 分、交通費は {info["fare"]} です。')
	print("\n")
# 出力するとき、 xxxから分部分は物件名？を出力したい。
# 所要時間、駅までの時間になっているので、駅からn 分歩く時間を追加して表示する

# 仮データ
# print(google_map.get_route_info(point_a, point_x))