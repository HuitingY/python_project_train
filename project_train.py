class Head:
    #架設車頭應有之資訊，包含車頭名字、列車長名字、燃料單位數、連節乘客車廂數以及next鍵，以便之後串聯乘客車廂。
    def __init__(self, name, headerName, oilNum, tail):
        self.name = name
        self.headerName = headerName
        self.oilNum = oilNum
        self.tail = tail
        self.next = None
    #功能3:顯示車頭車廂之資訊。
    def showInfo(self):
        print(f'車廂名字: {self.name};\n'
              f'列車長姓名: {self.headerName};\n'
              f'當前車頭燃料: 剩餘{self.oilNum}單位;\n'
              f'後面連結了{self.tail}節車廂\n'
              f'------------------------------------')
    #功能4:火車頭功能之行使時數。
    #使用者可以自行輸入駕駛小時，輸入完成後程式會自動檢查是否有足夠燃料。
    #燃料不足程式停止，若燃料充足則會顯示行駛時數以及剩餘燃料數。
    def driveHour(self):
        hours = int(input("請輸入駕駛時數："))
        if hours > 0:
            if (hours*10) > self.oilNum:
                print("欲行駛時數之所需燃料不足，請補充燃料")
            else:
                self.oilNum = self.oilNum - (hours*10)
                print(f'總共駕駛{hours}小時;\n'
                      f'還剩下{self.oilNum}單位的燃料!')
        else:
            print("輸入小時不可以為0或負數!")
    #功能7:補充燃料
    #使用該功能會自動將車頭之燃料束補充至100。
    def refuel(self):
        self.oilNum = 100
        print("火車燃料已加滿")

class Coach:
    #架設乘客車廂之應有資訊，包含名字、乘客人數以及next鍵以供之後連節其他乘客車廂。
    def __init__(self, name, passengersNum):
        self.name = name
        self.passengersNum = passengersNum
        self.next = None
    #功能3:顯示乘客車廂之資訊。
    def showInfo(self):
        print(f'車廂名: {self.name}車廂;\n'
              f'車廂總人數: {self.passengersNum}/20人\n'
              f'------------------------------------')
    #乘客車廂之上車方法，使用者可以自行設定上車人數;
    #一開始會檢查輸入人數是否大於0，之後再檢查"上車人數+原本車廂人數"是否會大於乘客車廂之上限人數20人;
    #若超過20人，則會要求使用者重新輸入。人數符合上限規定則會顯示上車人次以及目前人數。
    def getOn(self):
        nums = int(input(f'請輸入{self.name}之上車人數:'))
        if nums > 0:
            while ( self.passengersNum + nums > 20):
                print("OPPS!上車人數大於車廂所能容納的20人囉!")
                nums = int(input(f'請輸入{self.name}之上車人數:'))
            self.passengersNum = self.passengersNum + nums
            print(f' {self.name} 一共有 {nums} 人次上車;\n'
                  f'現在共有 { self.passengersNum} 人在 {self.name} 車廂中.')
        else:
            print("人數一定要大於0哦!")
    #乘客車廂之下車方法，使用者可以自行設定下車人數;
    #一開始會檢查輸入人數是否大於0，之後再檢查"原本車廂人數-下車人數"是否會小於0人;
    #若小於0人，則會要求使用者重新輸入。人數符合規定則會顯示下車人次以及目前人數。
    def getOff(self):
        nums = int(input(f'請輸入{self.name}之下車人數:'))
        if nums >0:
            while ( self.passengersNum - nums < 0):
                print("OPPS!下車人數超過本來在車上的人...這樣很可怕QQ!")
                nums = int(input(f'請輸入{self.name}之下車人數:'))
            self.passengersNum = self.passengersNum - nums
            print(f' {self.name} 一共有 {nums} 人次下車;\n'
                  f'現在共有 { self.passengersNum} 人在 {self.name} 車廂中.')

class LL:
    #設定head
    def __init__(self, head):
        self.head = head
    #功能3: 顯示所有車廂狀態，會分別呼叫head以及coach之顯示資訊方法。
    def showAllInfo(self):
        current = self.head
        i = 0
        while current != None:
            i += 1
            if i ==1:
                print(f'------------------------------------\n'
                      f'這是第{i}節火車頭')
            else:
                print(f'這是第{i}節乘客車廂')
            current.showInfo()
            current = current.next

    #功能1:增加乘客車廂，使用者可以自訂乘客車廂名字，而預設初始人數為0。
    #使用while迴圈，當current.next無連結其他物件則會建立乘客車廂並將其連結。
    #此時物件車頭車廂之乘客車廂計數也會變動。
    def addCoachAtEnd(self):
        name = input("請輸入乘客車廂名字，乘客人數一率預設為0: ")
        previous = None
        current =self.head
        while current.next != None:
            previous = current
            current = current.next
        newCoach = Coach(name, 0)
        current.next = newCoach
        self.head.tail += 1

    #功能5: 乘客上車，呼叫每節乘客車廂之上車方法。
    #初始會檢查是否有乘客車廂，若無則返回主畫面;
    #進入while迴圈開始呼叫物件"乘客車廂"之上車方法,當current.next無連結其他物件(即為最後一節乘客車廂時)程式停止。
    def getOnAll(self):
        current = self.head
        if self.head.tail !=0:
            while current.next != None:
                current = current.next
                current.getOn()
            print('----上車乘客輸入完成----')
        else:
            print("尚未建立乘客車廂!")

    #功能6: 乘客下車，呼叫每節乘客車廂之下車方法。
    #初始會檢查是否有乘客車廂，若無則返回主畫面;
    #進入while迴圈開始呼叫物件"乘客車廂"之下車方法,當current.next無連結其他物件(即為最後一節乘客車廂時)程式停止。
    def getOffAll(self):
        if self.head.tail !=0:
            current = self.head
            while current.next != None:
                current = current.next
                current.getOff()
            print('----下車乘客輸入完成----')
        else:
            print("尚未建立乘客車廂!")

    #功能2: 刪除第k節車廂，使用者可以自訂欲刪除車廂。
    #條件式1: 不可以刪除第一節車廂，因火車頭不可以刪除。
    #條件式2-3: 限制使用者key入數值k之範圍
    #進入迴圈之後開始數車廂，當找到使用者欲刪除之第k節車廂會先檢查車上是否有人，若有人報錯，若無人則會成功移除車廂。
    def deleteCoach(self):
        num = int(input("要刪除第幾節車廂?(車頭為第1節，且不可刪!)"))
        if num == 1:
            print("車頭不能刪吼!!")
            return
        elif num < 1:
            print("車廂無法為0或是負數")
            return
        elif num-1 > self.head.tail:
            print("你沒那麼多車廂喔!")
            return
        previous = None
        current = self.head
        ct = 1
        while ct < num:
            previous = current
            current = current.next
            ct += 1
        if current.passengersNum > 0:
            print("OPPS!車廂上還有乘客!不能刪除")
            return
        previous.next = current.next
        current = None
        self.head.tail -= 1


#預設初始畫面為使用者介面，使用者需輸入火車頭製造商以及列長姓名；
# 燃料預設為100單位，後面無連接乘客車廂。

print(f'開火車囉~~~~~~~~~~~\n'
      f'先來建立車頭跟車廂吧!!\n')
name = input("請輸入車頭製造商：")
headerName = input("請輸入列車長姓名: ")
header = Head(name, headerName, 100,0)
boo = LL(header)
while True:
    print(f'\n'
          f'---------------------------------\n'
          f'現在有車頭了～請選擇要執行什麼功能:\n'
          f'1. 加乘客車廂到列車尾端。\n'
          f'2. 刪除第k節車廂(火車頭不可以刪除哦!)\n'
          f'3. 顯示列車狀態.\n'
          f'4. 行駛列車 (請輸入要開幾小時)\n'
          f'5. 乘客上車 (依序輸入每個乘客車廂要上車的人數，注意容量上限)\n'
          f'6. 乘客下車 (依序輸入每個乘客車廂要下車的人數，注意容量下限)\n'
          f'7. 火車頭燃料補充\n'
          f'----------------------------------\n')
    try:
        user = int(input(""))
        if user ==1:
            boo.addCoachAtEnd()
        elif user ==2:
            boo.deleteCoach()
        elif user ==3:
            boo.showAllInfo()
            exit = input("按一鍵返回主畫面")
        #行駛方法架設在車頭物件下
        elif user ==4:
            header.driveHour()
        elif user ==5:
            boo.getOnAll()
        elif user ==6:
            boo.getOffAll()
        # 補充燃油方法架設在車頭物件下
        elif user ==7:
            header.refuel()
        else:
            print("沒有此功能鍵喔!")

    except:
        print("輸入錯誤，返回主畫面")
