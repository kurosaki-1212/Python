# 顧客番号と氏名データを３件分入力し、
# 入力が完了した後、入力された3件のデータをすべて表示するプログラムを作成してください

# customersという名前のからの辞書
zisyo = {}
i = 0
for k in range(3):
    banngou = input("番号")
    namae = input("名前")
    zisyo.setdefault(banngou, namae)

for key, value in zisyo.items():
    print(key, value)