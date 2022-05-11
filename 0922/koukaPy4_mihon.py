try:
  #文字列の入力
  str = input('文字列を入力してください：')
  str += input('別の文字列を入力してください：')

  #結合した文字列と文字数の出力
  print('結合した文字列は', str, 'です')
  print('文字数は、', len(str), 'です')

  #要素を1つずつ出力
  for i in range(len(str)):
      print('{}番目の文字は{}です'.format(i+1, str[i]))

except IndexError:
  print("代入失敗しました")

else:
  print("出力終了")

finally:
  print("お疲れさまでした")