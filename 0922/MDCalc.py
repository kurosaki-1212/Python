# 二つの整数値を読み込んで乗算と除算を行う

# ２つのエラーケースに対応したい 
# ①ゼロ除算エラー
# ②型変換エラー（数字型データに変換できないデータ）
class MDC:

    # コンストラクタ
    # 引数を2個もらう
    def __init__(self, numa :int, numb :int):
        self.a = numa
        self.b = numb

    def calcing(self):
        # メソッド（関数）の中にtryを書く
        try:

            print('a * b は', self.a * self.b, 'です。')
            print('a / b は', self.a / self.b, 'です。')

        except ZeroDivisionError:
            print('ゼロの割り算はできません！')

        except ValueError:
            print('数字を入力してください')

        finally:
            print('終了します！')