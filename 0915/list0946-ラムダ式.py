"""２値の和を求めるラムダ式（その２）"""

a = int(input('整数a：'))
b = int(input('整数b：'))
print('aとbの和は', (lambda x, y: x + y)(a, b), 'です。')

# ラムダはこれだけ覚える！
# 「lambda 引数:返却値」

# パターン1
ltest = lambda x, y : x + y
print(ltest(1, 2))

# パターン2
print((lambda x, y : x + y)(1, 3))
