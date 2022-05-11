#リストに以下内容を格納し、リスト名を list1としてください。
#リスト内容：リンゴ、バナナ、みかん、キウイ
list1 = ("リンゴ","バナナ","みかん","キウイ")

#P178のList 7-3を参考に、list1の内容を一行ずつ表示するfor文を作成してください。
for i in range(len(list1)):
    print(i,list1[i])

print(" ")

#P178のList 7-4を参考に、list1の内容とインデックス値を一行ずつ表示するfor文を作成してください。
for i,ch in enumerate(list1):
    print(i,ch)

print(" ")

#P178のList 7-5を参考に、list1の内容とインデックス値を一行ずつ表示するfor文を作成してください。
for i,ch in enumerate(list1):
    print(i + 1,ch)
   
print(" ")

# for i,ch in enumerate(list1,1):
#     print(i,ch)

#P178のList 7-6を参考に、list1の内容を一行ずつ表示するfor文を作成してください。
for i in list1:
    print(i)