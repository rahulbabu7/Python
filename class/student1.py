class Student:
    def readData(self):
        self.rollno = int(input("Enter the roll"))
        self.mark1 = int(input("Enter the mark1"))
        self.mark2 = int(input("Enter the mark2"))
    def computeTotal(self):
        self.total = 0
        self.total = self.mark1 + self.mark2
        
    def printDetails(self):
        print(f"Roll = {self.rollno}")
        print(f"mark1 = {self.mark1}")
        print(f"mark2 = {self.mark2}")
        print(f"Total = {self.total}")

student = Student()
student.readData()
student.computeTotal()
student.printDetails()
