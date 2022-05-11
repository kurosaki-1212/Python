# 問１：リスト「points」の内容をforを使って一行ずつ表示するプログラムを書いてください。
points = [100, 5, 12, 20, 98, 47, 65, 51]

for i in points:
    print(i)

# 問２：問１で使用したリスト「points」の内容を昇順に並び替えて、
# forを使って、実行例のように「1つ目のデータ」と表示してから
# リストの内容を一行ずつ表示するプログラムを書いてください。
# 実行例：
# 1つ目のデータ：????
# 2つ目のデータ：????
points = sorted(points)
for i in range(len(points)):
    print(str(i+1) + "つ目のデータ:" + str(points[i]))
