# キーボードから入力された数が
# 2の倍数なら「fizz」
# 3の倍数なら「Buzz」
# 6の倍数なら「FizzBuzz」
# それ以外なら「それ以外です」
# と表示するプログラムを作成してください。

# 入力された数をnumに代入
num = input('整数を入力してください：')

# num の値をint型に変換してnumに代入
num = int(num)

# ifやelifを使ってそれぞれの数に応じた文字列を表示する
if num % 6 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Buzz")
elif num % 2 == 0:
    print("Fizz")