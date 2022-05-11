#整数を1つ入力し、1から指定された整数までの奇数の合計を求めるプログラムを以下のコメント文をヒントに作成しましょう

#①合計値を格納する変数totalをゼロで初期化
from typing import no_type_check


total = 0
#②開始数の変数start　1で初期化
start = 1

#③ 数値を入力してもらい、int型にキャストし変数endに代入する
end = int(input("整数は："))

# ④1からendまで1ずつ繰り返し処理を行う
# ⑤startからendまで繰り返す
# 　②の処理で start に1を入れているので、ここのwhileは 1からend（入力された数）までループする
while start <= end:
  #⑥ifを使って奇数かどうかの判定 2で割ったあまりが1なら奇数
  if end % 2 == 1:
    #⑦奇数だったらtotalに足し込む
    total += start
  #⑧startのインクリメント 1から順番に偶数か奇数か判定するため、カウントアップ
  start += 1
#⑨結果の表示
print('1から',end,'までの奇数の合計=',total)