# 第３引数のデフォルト値を「,」変更してください。
# 引数のデフォルト値の設定方法はP254を参考に。
def conbine_Str(a, b, c = ","):
    print(a, b, sep=c)

conbine_Str('〇', '△')
conbine_Str('や', 'ほ', 'ー')
