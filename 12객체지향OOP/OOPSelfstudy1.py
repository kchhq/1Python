class Car :
    color : ""
    speed = 0

    # self라는 키워드로 메소드 호출하는 주체에게 적용됨
    def upSpeed(self, value) :
        self.speed += value
        # self study 12-1 추가부분
        if (self.speed > 150) :
            self.speed = 150

    def downSpeed(self, value) :
        self.speed -= value

myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0
myCar2 = Car()
myCar2.color = "파랑"
myCar2.speed = 0
myCar3 = Car()
myCar3.color = "노랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상은 %s이며, 속도는 %d입니다.\n" % (myCar1.color, myCar1.speed))
myCar2.upSpeed(60)
print("자동차2의 색상은 %s이며, 속도는 %d입니다.\n" % (myCar1.color, myCar1.speed))
myCar3.upSpeed(0)
print("자동차3의 색상은 %s이며, 속도는 %d입니다.\n" % (myCar1.color, myCar1.speed))

# self study 12-1 추가부분
myCar1.upSpeed(150)
print("자동차1의 색상은 %s이며, 속도는 %d입니다." % (myCar1.color, myCar1.speed))

