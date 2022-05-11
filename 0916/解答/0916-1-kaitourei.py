# 問題：球の表面積を求めるプログラムを作成してください。
# ただし、円の半径は、１～100までの乱数を発生させること。
# 円周率はmathモジュールを利用して作成すること。
# また、球の表面積は小数点以下切り捨てにすること。



# ①ランダムモジュールをインポートしよう
# ヒント：P96 List4-6
import random

# ②mathオブジェクトをインポートして正確な円周率を pi という変数で使えるようにしよう。 
# ヒント：円周率であるπ（パイ）は、mathモジュールの中に変数として定義されている。
import math

# ③１～100までのランダムな数を発生させて、変数rdmに代入しよう
# ヒント：P96 List4-6 random.randinit～の行
rdm = random.randint(1, 100)

# ④rdm を半径とする、球の表面積を求める関数を定義しよう
# 球の表面積の求め方：4×円周率×半径
# 円周率：π、半径：rとも記載される
def getSphereArea(radius):
    """球の表面積を求める"""
    surface = 4 * math.pi * radius * radius
    return  surface

# 生成した乱数を表示しよう
print('生成した乱数：', rdm)

# 球の表面積を求める関数を呼び出し、結果をprintで表示しよう
# その際、小数点以下の切り捨てをmath.floorで行おう
areadata = getSphereArea(rdm)
areadata = math.floor(areadata)

print('半径', rdm, 'の球の表面積は、', areadata)
