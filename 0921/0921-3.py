# インスタンス変数 input_num を追加しコンストラクタで値を設定しよう
# ヒント：P313
# 引数名：name（str型）、input_num（int型）
class Uranai:
    # コンストラクタ（初期化の為の特別なメソッド）
    def __init__(self, name :str, input_num :int):
        """Uranaiクラスのコンストラクタ"""
        self.name = name
        self.input_num = input_num
    # omikujiメソッド
    def omikuji(self):
        # ユーザが入力した数字に応じて、表示を換える
        if self.input_num >= 10:
            print(self.name + 'さんの運勢は、大吉です')
        elif self.input_num < 5:
            print(self.name + 'さんの運勢は、中吉です')
        else:
            print(self.name + 'さんの運勢は、大凶です')

# 名前を入力してもらう
inname = input('名前を入力してください：')

# 好きな番号を入力してもらう
innum = int(input('1～10までの数字を入力してください：'))

# Uranaiクラスのインスタンスを生成し、
# インスタンス変数name, input_numに値をセット
uranai1 = Uranai(inname, innum)

# omikujiメソッドを呼び出す
uranai1.omikuji()