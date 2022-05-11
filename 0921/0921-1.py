# uranai関数をクラス化しよう。
# クラス名：Uranai

class Uranai:
    def omikuji(self):
        print('江戸川コナンさんの今日の運勢は大凶です')

# omikuji1という変数にUranaiクラスのインスタンスを代入
# omikuji1という名前でUranaiクラスが使えるようになった
omikuji1 = Uranai()
omikuji1.omikuji()

# 1)class 名称:で定義
# 2)インスタンス化しないと使えない
# 3)class内のメソッド（関数）の第一引数はself
# 4)class内のメソッドを呼び出すときは、インスタンス名.メソッド名()

# Uranaiクラスのインスタンスを生成しよう

# omikujiメソッドを呼び出そう

