# じゃんけんゲーム、数あてゲームをインポート
# 別ファイルは呼び出し元のスクリプトファイルと同じフォルダに入れておく
import Janken, Number

# じゃんけんゲームのインスタンスを生成
janken = Janken.JankenPlay()

# 数あてゲームのインスタンスを生成
number = Number.NumberingGame(30)   #←このままだとエラーです

# 計算トレーニングのインスタンスを生成
while True:
    
    print('何をしますか？')
    print('1: じゃんけんする')
    print('2: 数当てチャレンジ')
    print('9: 終了する')

    act = int(input('整数で番号を入力:'))

    if act == 1:
        janken.action()

    elif act == 2:
        number.action()

    elif act == 9:
        print('また来てね')
        break
