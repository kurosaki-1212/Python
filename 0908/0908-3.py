# 文字列内の全文字を順に表示（その１：エラー）

s = 'ABCDEFG'

print('s[0] = ', s[0])
print('s[1] = ', s[1])
print('s[2] = ', s[2])
print('s[3] = ', s[3])
print('s[4] = ', s[4])
print('s[5] = ', s[5])
print('s[6] = ', s[6])
# print('s[7] = ', s[7])    # エラー

#逆順に表示
print('s[-7] = ', s[-7])
print('s[-6] = ', s[-6])
print('s[-5] = ', s[-5])
print('s[-4] = ', s[-4])
print('s[-3] = ', s[-3])
print('s[-2] = ', s[-2])
print('s[-1] = ', s[-1])
print('s[0] = ', s[0])

#問題：文字「D」を取り出す方法を「s[?]」の形式で、2種類記載してください。
print(s[3])
print(s[-4])
print(s[6])
print(s[-1])