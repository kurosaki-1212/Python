# Uranaiクラスにコンストラクタを追加しよう。
# インスタンス変数 name を追加しコンストラクタで値を設定しよう
# ヒント：P313
# 引数名：name（str型）
class Uranai:
    def omikuji(self):
        print(name + 'さんの今日の運勢は大凶です')


# Uranaiクラスのインスタンスを生成し、
# インスタンス変数nameに好きな名前を代入しよう
uranai1 = Uranai()


# omikujiメソッドを呼び出そう
uranai1.omikuji()