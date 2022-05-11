#P142辺りの内容
#文字列の操作（代表的なものだけ）

text1 = 'ABCDEFG'
d1 ='AB'
d2 ='0'
disp1 = 'text1[{}]に{}が含まれます'
disp2 = 'text1には{}は含まれません'

s = ''

# P139の「in」を使うと、文字列の中に特定の文字列が含まれるかわかる
# 「.find」は対象となる文字列の中に文字が含まれる位置がわかる
if d2 in text1:
    s = disp1.format(text1.index(d1),d1)
else:
    s = disp2.format(d1)

print(s)