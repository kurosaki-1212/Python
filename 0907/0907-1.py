# 1から、入力された数までの中で、
# 2の倍数なら「Fizz」
# 3の倍数なら「Buzz」
# 2の倍数でもあり、3の倍数でもあるなら「FizzBuzz」
# それ以外なら「それ以外です」
# と表示するプログラムを作成してください。

# 入力された数をnumに代入
num = input('整数を入力してください：')

# num の値をint型に変換してnumに代入
num = int(num)
counter = 1 
# whileを使って、numまでループする繰り返し構文を作成
# カウンターは変数counterを使う
while counter <= num:
    if counter % 6 == 0:
        print("FizzBuzz")
    elif counter % 3 == 0:
        print("Buzz")
    elif counter % 2 == 0:
        print("Fizz")
    else:
        print("それ以外です")

    # ifやelifを使ってそれぞれの数に応じた文字列を表示する


    # counterをインクリメント（1増加させる）
    counter += 1