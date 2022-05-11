#整数を1つ入力し、1から指定された整数までの奇数の合計を求めるプログラムを作成してください
from typing import no_type_check


total = 0
start = 1

end = int(input("整数は："))
while start <= end:
  if start % 2 == 1:
     total += start
  start += 1
print('1から',end,'までの奇数の合計=',total)
