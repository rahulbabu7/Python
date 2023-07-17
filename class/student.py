class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    def dataprint(self):
        print(f"name = {self.name}")
        print(f"roll = {self.roll}")
std1 = Student("rahul",20)
std2 = Student("rono",20)

std1.dataprint()
std2.dataprint()