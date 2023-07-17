class Arith:
    def read(self):
        self.a = int(input("Enter the first num"))
        self.b = int(input("Enter the second num"))
    def add(self):
        sum = 0
        sum = self.a+self.b
        print(sum)
arith = Arith()
arith.read()
arith.add()