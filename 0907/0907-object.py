
n = 17
print(id(n))
print(id(17))

# 変数に値を代入＝正確にはオブジェクトの参照を設定
num1 = 5
num2 = 3.14
moji1 = '(^o^)ノ'

# オブジェクトIDを表示
print(id(5))
print(id(num1))

print(id(6))
print(id(num1 + 1))

print(id(3.14))
print(id(num2))

print(id('(^o^)ノ'))
print(id(moji1))

# オブジェクト(数、文字列)を指定した場合も、
# 変数を指定した場合も同様のオブジェクトIDが表示されることを確認する