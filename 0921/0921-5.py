class TalkRobot:
    def __init__(self, name):
        self.name = name
    
    def sayOhayo(self):
        print(self.name + 'さん、おはよう')

    def sayKonnichiha(self):
        print(self.name + 'さん、こんにちは')

# 「STalkRobot」を継承
class TalkRobo2(TalkRobot):    
    pass

# 継承元（スーパークラス＝基底クラス）のコンストラクタが使える
robo = TalkRobo2('ジョージ') 
robo.sayOhayo()
robo.sayKonnichiha()  