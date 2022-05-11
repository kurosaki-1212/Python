# uranai関数をクラス化しよう。
# クラス名：Uranai
class Uranai:
    def omikuji(self):
        print('江戸川コナンさんの今日の運勢は大凶です')

# omikuji()

# Uranaiクラスのインスタンスを生成しよう
uranai1 = Uranai()
# Uranai.omikuji のようには使えない！
# →classはインスタンス化しないとつかえないから

# omikujiメソッドを呼び出そう
uranai1.omikuji()