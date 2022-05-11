# リストを作成する時は[]
# タプルは()
# 辞書は{}を使う
# 辞書は、キーと値を組み合わせたdictionary（辞書）



# みかん、りんご、バナナ、イチゴのデータを追加しよう
fruits = {
    "11" : "みかん",
    "22" : "リンゴ",
    "33" : "バナナ",
    "44" : "イチゴ",
}

# setdefaultメソッドを使って、fruits辞書に
# もも、ぶどうのデータを追加しよう。
# ヒント：P219 
# さらにヒント：下の例はfruitsにキー：100,値：オレンジを追加する方法
fruits.setdefault('100', 'オレンジ')
fruits.setdefault('55', 'もも')
fruits.setdefault('66', 'ぶどう')
print(fruits)

# getメソッドを使ってキーが22の値を変数 data1に代入しよう
# ヒント：P218
# さらにヒント：下の例はdata1にfruits辞書からキー値が100のデータを代入している
data1 = fruits.get('100')
print(data1)
data2 = fruits.get('22')
print(data2)

# updateメソッドを使ってキーが44の値を「青りんご」に変更しよう
# ヒント：P220

# fruits.update(44 = "青りんご")
# print(fruits)

# fruits辞書の内容をforを使ってすべて画面に表示しよう
# ヒント：P223
for i, key in enumerate(fruits):
    print("{} {}".format(i, key))

for i, key in enumerate(fruits, 1):
    print("{} {}".format(i, key))

for key in fruits:
    print("{}".format(key))

for item in fruits.items():
    print(item)

