# 例：文字列の繰り返し
# 文字列の中に文字列を埋め込む場合は、formatを使う

#例文：彼の名前はXXです。YY歳です。
# 上記例文のXX部分に「みーちゃん」、YYに「9」を入れて表示したい

ex = '彼の名前は{}です。{}歳です。'
ex1 = ex.format('みーちゃん','9')
print(ex1)

#問題
#入力された3つの商品名を、「XXは売り切れです」という文字列のXXの部分に埋め込んで表示してください。
#ただし、formatを使うこと

data = '{}は売り切れです'

m1 = input('一個目の商品を入力してください:')
m2 = input('二個目の商品を入力してください:')
m3 = input('三個目の商品を入力してください:')

#ここに3つの商品に対して「XXは売り切れです」と表示する
print(data.format(m1))
print(data.format(m2))
print(data.format(m3))