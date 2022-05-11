# キーボードから入力された値が偶数なら「even」奇数なら「odd」と表示するプログラムを作成しよう
n = int(input("整数を入力してください。"))
if n % 2 == 0:
    print("even")
else:
    print("odd")