# 二つの整数値を読み込んで乗算と除算を行う

# ２つのエラーケースに対応したい 
# ①ゼロ除算エラー
# ②型変換エラー（数字型データに変換できないデータ）

try:
    a = int(input('整数a：'))
    b = int(input('整数b：'))

    print('a * b は', a * b, 'です。')
    print('a / b は', a / b, 'です。')

except ValueError:
    print("整数と認識出来ません！")

except ZeroDivisionError:
    print("ゼロによる除算！")

else:
    print("正常終了！")
    
finally:
    print("お疲れさまでした。")