#リストに以下内容を格納し、リスト名を list1としてください。
#リスト内容：リンゴ、バナナ、みかん、キウイ
list1 = ["リンゴ","バナナ","みかん","キウイ"]
x = list1[0] # リンゴがxに代入される
# リストに以下内容を格納し、リスト名を list2としてください。
# ただし、リスト作成時には、list関数を使用すること
# リスト内容：90,1,100,-39,15,83,4444(すべて整数)
# ヒント：P166 list関数によるリストの生成
list2 = list([90,1,100,-39,15,83,4444])
y = list2[3] # -39がyに代入される

#list関数とrangeを使って指定した範囲の数が格納されたリストを作成し、リスト名をlist3にしてください。
# リスト内容：0,1,2,3,4,5,6,7,8,9,10
# ヒント：P166 list関数によるリストの生成
list3 = list(range(11))

s = [1,2,3,4,5,6,10,11]
i = len(s)
print(i)