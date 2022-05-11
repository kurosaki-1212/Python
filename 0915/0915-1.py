# デバッグしながら実行してみよう(ステップインF11)
# 関数名：calcAdd
# 引数(ひきすう)：
# 　a :１つ目の足し算の値（int型）
# 　b :２つ目の足し算の値（int型）
def calcAdd(a, b):
    c = a + b
    print(a,'+', b, '= ', end ='')
    print(c)
# calcAddの範囲はここまで

# print(1 + 3)
# print(2 + 100)
# print(1, '+', 3, '=', 1 + 3)

# 関数を呼び出す
#　--> calcAddを、引数（ひきすう）に1と3を渡して呼び出す
# 1 + 3 を表示
calcAdd(1, 3)

# 2 + 100を表示
calcAdd(2, 100)

# calcAddを使って -50 + 800を表示しよう
calcAdd(-50, 800)
