# 0915-1.pyを参考に
# 引数の二つの文字列を連結して返却する関数を作成しよう
# 関数名：conbine_Str
# 引数：
# 　a :一つ目の文字列
# 　b :二つ目の文字列
# 返却値：aとbを結合した文字
def conbine_Str(a, b):
    c = a + b
    return c  # return a + b  とも書ける


# conbine_Str を呼び出して、変数 str1 に代入しよう。
# conbine_Strの引数は「aaa」と「bbb」とします
str1 = conbine_Str("aaa", "bbb")
print(str1)