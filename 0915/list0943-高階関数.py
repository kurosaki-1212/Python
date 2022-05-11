"""一つの名前で二つの関数を呼び出す"""

def mul2(x, y):
    return x * y

def add2(x, y):
    return x + y

a = int(input('整数a：'))
b = int(input('整数b：'))

func = mul2
print('aとbの積は', func(a, b), 'です。')

func = add2
print('aとbの和は', func(a, b), 'です。')

# 高階関数は、関数を関数に渡すことができる機能
# 実装の切り替えを容易にする目的でよく使われている