try:
    # ファイルをインポートする
    import Janken, Number, Item, Year

    # ファイルの中のクラスを呼び出す
    janken = Janken.JankenGame()

    number = Number.NumberGame(50)

    item = Item.Lucky()

    year = Year.Nengou


    while True:

        # 遊ぶ内容を選んでもらう
        print("何で遊ぶ？")
        print("１：じゃんけん")
        print("２：数当てゲーム")
        print("３：明日のラッキーアイテム")
        print("４：西暦から和暦を調べる")
        print("０：終了する")

        # 選んだ値を入力してもらう
        choice = int(input("数字を入れてね！"))

        # 1だった場合「じゃんけん」をやる
        if choice == 1:
            janken.action()

        # 2だった場合「数当てゲーム」をやる
        elif choice == 2:
            number.action()

        # 3だった場合「明日のラッキーアイテム」をやる
        elif choice == 3:
            item.action()

        # 4だった場合「西暦から和暦を調べる」をやる
        elif choice == 4:
            year.action()

        # 0だった場合処理を終了する
        elif choice == 0:
            print("また遊ぼう！")
            break

# 文字が入力されたときの例外処理
except ValueError:
    print("指定された数字を入力してください")

# 処理が終了したときの出力
finally:
    print("お疲れ様でした！")