
#数字を入力し、入力した数だけ画面に■印を表示するプログラムを書いてください。
#   
#実行結果
#  数を入力してください: 7
#  ■■■■■■■
n = int(input('数を入力してください:'))

print(str(n)+':',end='') # 改行しない出力
for i in range(n):
    print('■',end='')
