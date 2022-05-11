# 文書化文字列とアノテーションの練習 P266～
# 0915-3.pyのcalcAdd2にアノテーションを付けた例

# 関数名：calcAdd2
# 引数：
# 　a :１つ目の足し算の値（int型）
# 　b :２つ目の足し算の値（int型）
# 返却値：a + b の結果（int型）
def calcAdd2(a: int, b: int) ->int: #アノテーション
    """二つの引数の合計を返却する"""  # 文書化文字列
    c = a + b
    return c

# アノテーションと異なる型が引数に設定されていた場合は…？
a = calcAdd2(1, 2)
# b = calcAdd2('1', '2')

# 文書化文字列をhelp関数で表示してみる
help(calcAdd2)