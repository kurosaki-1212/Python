class Uranai:

    def __init__(self, name :str, input_num :int):
        """Uranaiクラスのコンストラクタ"""
        self.__name = name
        # ユーザが入力した数をセット
        self.input_num = input_num

    def omikuji(self):
        # ユーザが入力した数字に応じて、表示を換える
        if self.input_num >= 10:
            print(self.__name + 'さんの運勢は、大吉です')
        elif self.input_num < 5:
            print(self.__name + 'さんの運勢は、中吉です')
        else:
            print(self.__name + 'さんの運勢は、大凶です')
    
    @property
    def name(self):
        """名前データを取得（nameの中身を取得＝ゲッタ）"""
        return self.__name
    
    @name.setter
    def name(self, name_data):
        """名前データを設定（nameに値を設定する＝セッタ）"""
        self.__name = name_data

# 名前を入力してもらう
inname = input('名前を入力してください：')

# 好きな番号を入力してもらう
innum = int(input('1～10までの数字を入力してください：'))

# Uranaiクラスのインスタンスを生成し、
# インスタンス変数name, input_numに値をセット
uranai1 = Uranai(inname, innum)

# omikujiメソッドを呼び出す
uranai1.omikuji()

# setterを呼び出して、別の人の名前に変更する
uranai1.name = 'ルークスカイウォーカー'

# omikujiメソッドを呼び出す
uranai1.omikuji()

# 同様に、input_numのgetterとsetterを設定してみよう