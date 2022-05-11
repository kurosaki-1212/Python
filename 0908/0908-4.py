# len関数のまとめ
# lenはlengthの略で、文字列の長さを取得して返す

print('(1)')
b ='abcdefghijk'
c = len(b)
print(b, 'は',str(c),'文字です。')

print('(2)')
a ='テスト頑張ろう'
print(a,'は{}文字です。'.format(len(a))) # テスト頑張ろうは７文字です

print('(3)')
#(3)文字列分繰り返して、一文字ずつ表示する
t = 'あいうえお'
tlen = len(t)
for i in range(tlen):
    print(t[i])

print('(4)')
#(4)文字列分繰り返して、一文字ずつ表示する→1)と同じ内容
t = 'あいうえお'
for i in range(len(t)):
    print(t[i])