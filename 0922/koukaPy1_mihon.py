try:

  #半径を入力してもらい、float型にキャストして変数radに代入
  rad = float(input('球の半径を入力してください(cm):'))

  #球の体積を計算し、四捨五入してvolに代入
  vol = round((4/3) * 3.1415 * rad * rad * rad)

  #球の体積を表示
  print('球の体積は', vol, 'cm3です。', sep='')
  
  #球が大きいか小さいかの判定
  if vol>4200:
      #4200よりも大きい場合
      print('この球は大きいです。')
  else:
      #4200よりも小さい場合
      print('この球は小さいです。')

except ValueError:
  print("型が違います")

else:
  print("計算完了")

finally:
  print("お疲れさまでした")
