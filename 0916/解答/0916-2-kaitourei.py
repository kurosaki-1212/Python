# 顧客番号と氏名データを３件分入力し、
# 入力が完了した後、入力された3件のデータをすべて表示するプログラムを作成してください

customers = {}
i = 0
while i <= 2:
    #出席番号を入力
    custcode = input('顧客番号を入力してください：')
    #名前を入力
    name = input('氏名を入力してください：')

    #顧客番号をキー、氏名をバリューとして辞書に保存する
    customers.setdefault(custcode, name)

    # カウントアップ
    i += 1

#商品コード、名称をforで走査し表示する
# ヒント：テキストP225
for key, value in customers.items():
  print("顧客番号", key, "：", value ,sep = "")
