# ランダムモジュールをインポートして使ってみよう
# ヒント：P96 List4-6
import random as ran

# ランダムモジュールのrandintを使ってみよう。
rannum = ran.randint(1, 100)
print(rannum)

# mathモジュールをインポートして円周率 pi という名前で使えるようにしてみよう
import math
print(math.pi)

# ①1～1000までの乱数を発生させて、printで表示してみる
# 使い方はパイソンのリファレンスサイトを見てみる！
runnum = ran.randint(1, 1000)
print(runnum)

# ②piを使って、①で発生させた乱数を半径とする円の面積を求めて、表示しよう
# 円の面積の求め方：pi * r * r　(r =　半径)
en = math.pi * runnum * runnum
print(en)

# ①で求めた円の面積をmath.floorを使って小数点以下の切り捨てを行ってください
# 結果をprintで表示してください
syousuu = math.floor(en)
print(syousuu)

# ①で求めた円の面積の小数点以下に切り捨てた値を
# ３桁のカンマ区切りで表示してください
# ヒント：157p
print("{:,}".format(syousuu))
