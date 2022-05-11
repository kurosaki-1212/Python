# スライスの練習
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

r1 = s[0:6]
print('r1:',r1)  #index:0から5まで、0から6文字分

r2 = s[0:10:2]
print('r2:',r2)  #index:0から9まで、0から10文字分、1こ飛ばし（1だと刻み幅なし、2だと2こずつ刻み）

r3 = s[5:20:3]   #indexから5から19まで、5から20文字分、2こ飛ばし
print('r3:',r3)

r4 = s[12:5:-1] #indexから12から6まで、12から後ろに7文字分
print('r4:',r4)