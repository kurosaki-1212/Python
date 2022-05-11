# zip関数の確認
names = ['太郎', '正雄', 'ヨシヒコ']   # リスト
ages = (21, 19, 22)      # タプル
likes = ['白米', '肉', '甘いもの']

# zip関数でまとめる
zp1 = zip(names, ages)
# zip関数で代入できるのはzip型なので、そのままは表示できない
print(zp1)

# zp1をタプルとしてまとめたリストにできる…
newlist = list(zp1)
print('新しいリスト：', newlist)
print(type(newlist))

# リスト同士のzip化
zp2 = zip(names, likes)
newlist2 = list(zp2)
print('新しいリスト：', newlist2)

