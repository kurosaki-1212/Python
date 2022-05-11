class TalkRobot:
    def __init__(self, name):
        self.name = name
    
    def sayOhayo(self):
        print(self.name + 'さん、おはよう')

    def sayKonnichiha(self):
        print(self.name + 'さん、こんにちは')

# 「STalkRobot」を継承
class TalkRobo2(TalkRobot):    
    def __init__(self, name, keisyo):
        super().__init__(name)
        # 自分のクラスのみに使用する変数
        self.keisyo = keisyo
    
    def sayKonbanha(self):
        print(self.name + self.keisyo + "、こんばんは")

# 継承元（スーパークラス＝基底クラス）のコンストラクタが使える
robo = TalkRobo2('ジョージ', "ちゃん") 
robo.sayKonnichiha()

# 派生クラスのメソッドを呼び出す
robo.sayKonbanha() 