# P36 List2-11の内容を入力しよう。
# それぞれの行が何をやっているのかコメントを追加しよう

#キーボードから整数の値を入力してもらい、変数sに変換する。
s = input('整数a：')

#変数Sはまだ文字型なので、int型に変換して整数aに代入する。
a = int(s)

#二つ目の値を入力してもらい、変数sに変換する。
s = input('整数b：')

#変数Sはまだ文字型なので、int型に変換して整数bに代入する。
b = int(s)

# a と b の加算
print('a + b は',  a + b,  'です。') 
# a と b の減算
print('a - b は',  a - b,  'です。')
# a と b の乗算 
print('a * b は',  a * b,  'です。')
# a と b の除算
print('a / b は',  a / b,  'です。') 
# a と b の切り捨て除算
print('a // b は', a // b, 'です。') 
# a と b の剰余算
print('a % b は',  a % b,  'です。')
# a と b のべき乗
print('a ** b は', a ** b, 'です。')