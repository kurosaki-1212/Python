#リストの便利な使い方を覚えましょう
#ヒント：テキストP174～

from typing import Reversible


lst1 = [100, 30, 55, 10, 7, 22, 0, 84]

# .appnedを使って、リストの最後に 400 を追加しましょう（P174）
lst1.append(400)

# .insertを使って、4番目の要素 の後ろに 6 を追加しましょう（P176）
lst1.insert(4, 6)

# .remove を使って、リストの内容が55の要素を削除しよう （P176）
lst1.remove(55)

# max関数を使って、リスト内の最大値をprintで出力しよう（P183）
print('リスト内のの最大値は' + str(max(lst1)))

#sortedを使ってリストの内容をソート（並び替え）しましょう
#ヒント：P72
# sortedを使って降順(reverse=True)に並び替える
lst1 = sorted(lst1, reverse = True)

#リストのすべての内容を表示しましょう
print(lst1)