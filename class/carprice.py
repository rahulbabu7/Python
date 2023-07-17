class Car:
    def __init__(self,model,year,price):
        self.model = model
        self.year = year
        self.price = price
    def cost(self):
        print(f"cost ={self.price} ")
car = Car("Agera",2020,16000000)
car1 = Car("Genera",2020,14000000)

car.cost()
car1.cost()


