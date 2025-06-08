class Car :
    speed = 0

    def Upspeed(self, value) :
        self.speed += value

        print("현재 속도(슈퍼 클래스) : %d" % (self.speed))

class Sedan(Car) :
    def Upspeed(self, value) :
        self.speed += value
        
        if (self.speed>150) :
            self.speed = 150

        print("현재 속도(서브 클래스) : %d" % (self.speed))

class Sonata(Sedan) :
    def Upspeed(self, value) :
        self.speed += value
        
        if (self.speed>150) :
            self.speed = 150

        print("현재 속도(서브 클래스) : %d" % (self.speed))

class Truck(Car) :
    pass

truck1, sedan1, sonata1 = None,None,None

truck1 = Truck()
sedan1 = Sedan()
sonata1 = Sonata()

print("트럭 --> ", end = " ")
truck1.Upspeed(200)
print("승용차 --> ", end = " ")
sedan1.Upspeed(200)
print("소나타 --> ", end = " ")
sonata1.Upspeed(200)


