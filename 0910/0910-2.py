test1 = 'いろはにほへと'
for i in range(len(test1)):
    print(i, test1[i])

print('')

#enumerateの練習
for i,ch in enumerate(test1):
    print(i,ch)

print('')

#リストを使ったenumerate
test2 = ['いろはにほへと', 'ちりぬるを','わかよたれそ','つねならむ']
for i, name in enumerate(test2):
    print(i, name)