#List3-5の条件を変更しよう。
# ①n が10以上なら「大きい数が入力されました」と表示
# ②n が0なら「0が入力されました」と表示
# ③n が-10以下なら「小さい数が入力されました」と表示
# ④それ以外なら「ノーコメント」と表示しよう。
# ① or ② or ③ or ④ が終わった後、「おつかれさまでした！」と表示しよう
n = int(input("整数値："))

if n > 10:
    print("大きい数が入力されました。")
elif n == 0:
    print("0が入力されました。")
elif n < -10:
    print("小さい数が入力されました。")
else:
    print("ノーコメント")
print("お疲れさまでした！")