import threading

class Adder(threading.Thread):
    def __init__(self, name, targetnum):
        super().__init__()
        self.AdderName = name
        self.targetnum = targetnum

    def run(self):
        sumnum = sum(range(1, self.targetnum + 1))
        print(f"\n1+2+3+......+ {self.AdderName} = {sumnum}")

Adder1 = Adder("Adder1", 100)
Adder2 = Adder("Adder2", 1000)
Adder3 = Adder("Adder3", 10000)

Adder1.start()
Adder2.start()
Adder3.start()

#출력 순서 고정시키기 위해 메인 쓰레드 멈춰두기
Adder1.join()
Adder2.join()
Adder3.join()
