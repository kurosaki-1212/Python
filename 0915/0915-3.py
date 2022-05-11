# デバッグしながら実行してみよう
# 関数名：calcAdd2
# 引数：
# 　a :１つ目の足し算の値（int型）
# 　b :２つ目の足し算の値（int型）
# 返却値：a + b の結果（int型）
def calcAdd2(a, b):
    c = a + b
    # 関数を終了して、プログラムを呼び出し元に戻し、値cを返却する
    return c


# 返却値がある関数を呼び出す
#　--> calcAdd2を、引数（ひきすう）に1と3を渡して呼び出す
# 1 + 3 の結果が返却されansに代入される
ans = calcAdd2(1, 3)
print(ans)
print(calcAdd2(2, 4))

# calcAdd2を使って2 + 100の結果を変数ans2に代入しよう
ans2 = calcAdd2(2, 100)
print(ans2)
print(calcAdd2(2, 100))

