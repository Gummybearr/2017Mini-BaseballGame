class player:
    def hit(self,name,hitpercent):
        self.name = name
        import random
        luck = int(random.random()/0.5)
        if luck == 1:
            self.hitpercent = float(hitpercent+0.1)
        else:
            self.hitpercent = float(hitpercent-0.1)
        data = [self.name,self.hitpercent]
        return data
    def pitch(self,name,pitchpercent):
        self.name = name
        import random
        luck = int(random.random()/0.5)
        if luck == 1:
            self.pitchpercent = float(pitchpercent)+0.1
        else:
            self.pitchpercent = float(pitchpercent)-0.1
        data = [self.name,self.pitchpercent]
        return data

#선수 만들기
man_1,man_2,man_3,man_4,man_5,man_6,man_7,man_8,man_9 = player(),player(),player(),player(),player(),player(),player(),player(),player()
man_1.pitch("John",1.2), man_2.hit("James",0.3), man_3.hit("Jade",0.25)
man_4.hit("Jason",0.17), man_5.hit("Josh",0.26), man_6.hit("Jade",0.33)
man_7.hit("Jiggy",0.4), man_8.hit("Jimmy",0.1), man_9.hit("Jeff",0.19)

man_a,man_b,man_c,man_d,man_e,man_f,man_g,man_h,man_i = player(),player(),player(),player(),player(),player(),player(),player(),player()
man_a.pitch("Daniel",1.6), man_b.hit("Drogba",0.2), man_c.hit("Dean",0.4)
man_d.hit("Dash",0.27), man_e.hit("Diego",0.22), man_f.hit("Dyson",0.19)
man_g.hit("Dobby",0.33), man_h.hit("Dumbledore",0.5), man_i.hit("Draco",0.01)

class team:
    def __init__(self):
        self.team = []
    def lineup(self,a,b,c,d,e,f,g,h,i):
        self.team.append(a), self.team.append(b), self.team.append(c)
        self.team.append(d), self.team.append(e), self.team.append(f)
        self.team.append(g), self.team.append(h), self.team.append(i)
        return self.team
    def teamlist(self):
        return self.team
    def teamname(self,name):
        self.name = name
        return self.name
    def showteamname(self):
        return self.name

#팀 만들기    
team_1,team_2 = team(),team()
team_1.lineup(man_1,man_2,man_3,man_4,man_5,man_6,man_7,man_8,man_9)
team_1.teamname("삼성 라이온즈")
team_2.lineup(man_a,man_b,man_c,man_d,man_e,man_f,man_g,man_h,man_i)
team_2.teamname("기아 타이거즈")

#게임과 해설
class gameandnarration:
    def __init__(self,team_1,team_2):
        self.out = 0
        self.eaning = 1
        self.score_1 = 0
        self.score_2 = 0
        self.onfield = 0
        self.highestfield = 0
        self.count_1 = 0
        self.count_2 = 0
        self.team_1 = team_1
        self.team_2 = team_2
    def startingmusic(self):
        import os
        os.system("start sound.wav")
        print("(음악 큐!)")
        import time
        time.sleep(3)
    def greetings(self):
        print("안녕하십니까 야구를 사랑하시는 시청자 여러분, 반갑습니다. 여기는 인포매틱스 스타디움입니다!")
        import time
        time.sleep(1)
        print(self.team_1.showteamname(),"과(와)",self.team_2.showteamname(),"의 경기가 진행됩니다.")
        time.sleep(1)
    def eaningannounce(self):
        import time
        if self.eaning%2==1:
            print("경기는",int(self.eaning/2)+1,"회 초")
            time.sleep(1)
        else:
            print("경기는",int(self.eaning/2),"회 말")
            time.sleep(1)
    #공수 결정
    def firstaord(self):
        import random
        luck = int(random.random()/0.5)
        if luck ==1:
            self.attack = self.team_1 
            self.defend = self.team_2
            return self.attack.showteamname()
        else:
            self.attack = self.team_2
            self.defend = self.team_1
            return self.attack.showteamname()
    def aordannounce(self):
        print(self.attack.showteamname(),"팀이 공격을 시작합니다!")
        import time
        time.sleep(1)
    #누가 공던지고 누가 칠지
    def playercount(self):
        self.playercount_1 = (self.count_1%8)+1
        self.playercount_2 = (self.count_2%8)+1
        self.playercountthistime = 0
        if self.attack == self.team_1:
            self.pitcher = self.team_2.teamlist()[0]
            self.hitter = self.team_1.teamlist()[self.playercount_1]
            self.playercountthistime = (self.count_1%8)+1
            self.count_1 +=1
        else:
            self.pitcher = self.team_1.teamlist()[0]
            self.hitter = self.team_2.teamlist()[self.playercount_2]
            self.playercountthistime = (self.count_2%8)+1
            self.count_2 +=1
        return [self.pitcher,self.hitter]
    #필드 상황 보여주기
    def status(self):
        print("필드에는",self.onfield,"명이 있습니다")
    def playerannounce(self):
        import time
        print("마운드에 올라서는",self.playercountthistime,"번 타자",self.hitter.name+"!")
        time.sleep(0.5)
        print("투수는",self.pitcher.name,"입니다!")
        time.sleep(0.5)
        print("공 던집니다!")
        time.sleep(0.5)
    #대결
    def versus(self):
        import random
        luck = random.random()
        percent = self.hitter.hitpercent*self.pitcher.pitchpercent
        if percent<luck:
            self.out +=1
            self.result = "아웃!"
            print("아웃!")
        elif (percent>=luck) and (percent<luck+0.1):
            self.result = "1루타!"
            print("1루타!")
        elif (percent>luck) and (percent>=luck+0.1) and (percent<luck+0.15):
            self.result = "2루타!"
            print("2루타!")
        elif (percent>luck) and (percent>=luck+0.15) and (percent<luck+0.2):
            self.result = "3루타!"
            print("3루타!")
        else:
            self.result = "홈런!"
            print("홈런!")
    #출루
    def moveon(self):
        if self.result =="홈런!":
            self.onfield += 1
            self.highestfield += 4
        elif self.result =="1루타!":
            self.onfield +=1
            self.highestfield +=1
        elif self.result =="2루타!":
            self.onfield +=1
            self.highestfield +=2
        elif self.result =="3루타!":
            self.onfield +=1
            self.highestfield +=3
    #점수 산정
    def points(self):
        if self.result == "홈런!":
            while True:
                if self.attack == team_1:
                    self.score_1 +=1
                    print(self.attack.showteamname(),"팀이 1점을 내었습니다!")
                else:
                    self.score_2 +=1
                    print(self.attack.showteamname(),"팀이 1점을 내었습니다!")
                self.onfield -= 1
                if self.onfield ==0:
                    self.highestfield = 0
                    break
        else:
            while self.onfield >=0 and self.highestfield-4 >= 0:
                self.onfield-=1
                self.highestfield -=1
                if self.attack == team_1:
                    self.score_1 +=1
                elif self.attack ==team_2:
                    self.score_2 +=1
                print(self.attack.showteamname(),"팀이 1점을 내었습니다!")
    def switch(self):
        if self.out ==3:
            print("이닝 종료! 공수 교대!")
    def neweaning(self):
        if self.out ==3:
            self.eaning +=1
            self.out = 0
            self.highestfield = 0
            self.onfield = 0
            if self.attack == self.team_1:
                self.attack = self.team_2
                self.defend = self.team_1
            else:
                self.attack = self.team_1
                self.defend = self.team_2
    def showscore(self):
        if self.score_1>self.score_2:
            print("현재 스코어",self.score_1,"대",self.score_2,"로",self.team_1.showteamname(),"팀이 앞서고 있습니다!")
        elif self.score_2>self.score_1:
            print("현재 스코어",self.score_2,"대",self.score_1,"로",self.team_2.showteamname(),"팀이 앞서고 있습니다!")    
        else:
            print("현재 스코어",self.score_1,"대",self.score_2,"로 양 팀 모두 팽팽한 승부를 펼치고 있습니다!")
        import time
        time.sleep(0.5)
    def winnerannounce(self):
        if self.score_1>self.score_2:
            print("최종 스코어",self.score_1,"대",self.score_2,"로",self.team_1.showteamname(),"팀이 이겼습니다!")
        elif self.score_2>self.score_1:
            print("최종 스코어",self.score_2,"대",self.score_1,"로",self.team_2.showteamname(),"팀이 이겼습니다!")    
        else:
            print("최종 스코어",self.score_1,"대",self.score_2,"로 무승부입니다!")
    def startgame(self,game):
        game.startingmusic()
        game.greetings()
        game.firstaord()
    def playgame_6(self,game):
        for i in range(6):
            test.eaningannounce()
            test.aordannounce()
            test.status()
            if self.eaning==6:
                while True:
                    test.playercount()
                    test.playerannounce()
                    test.versus()
                    test.moveon()
                    test.points()
                    if self.out==3:
                        print("경기 종료!")
                        test.winnerannounce()
                        break
            else:
                while True:
                    test.playercount()
                    test.playerannounce()
                    test.versus()
                    test.moveon()
                    test.points()
                    test.switch()
                    if self.out ==3:
                        test.neweaning()
                        test.showscore()
                        break

    
test=gameandnarration(team_1,team_2)
test.startgame(test)
test.playgame_6(test)

