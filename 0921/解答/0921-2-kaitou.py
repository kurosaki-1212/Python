# Uranaiクラスにコンストラクタを追加しよう。
# インスタンス変数 name を追加し、値を代入してみよう
# ヒント：P313
# 引数名：name（str型）
class Uranai:

    def __init__(self, name :str):
        """Uranaiクラスのコンストラクタ"""
        self.name = name

    def omikuji(self):
        print(self.name + 'さんの今日の運勢は大凶です')

# Uranaiクラスのインスタンスを生成し、
# インスタンス変数nameに好きな名前を代入しよう
uranai1 = Uranai('機関車トーマス')

# omikujiメソッドを呼び出そう
uranai1.omikuji()