# # from turtle import Turtle, Screen

# # timmy = Turtle()
# # print(timmy)
# # timmy.shape("turtle")
# # timmy.color("red")
# # timmy.forward(100)
# # timmy.left(200)

# # my_screen = Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()


# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("name", ['samir', 'prabin', 'saurab'])
# table.add_column("type", ["electric", "water", "Fire"])
# print(table.align)

# print(table)



# init is also called constructor 
class car:

    total_car = 0



    def __init__(self, brand, model): #__ init__ to put parameters # self --> to establish connection or access attributes within class
        self.__brand = brand
        self.__model = model
        car.total_car += 1 # to coount total object / car

#Encapsulation
# modify the CAr class to encapsulate the brand attribute making it private 
# and provide getter method fo it
    def get_brand(self):
         return self.__brand + " !"
    

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
         return "petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "cars are means of transport"
    @property
    def model(self):
        return self.__model
    
 # create an ElectricCar class that inheits form the Car class and has an additional attribute battery_size
   
class ElectricCar(car):
        def __init__(self, brand, model, battery_size):
            super().__init__(brand, model)
            self.battery_size = battery_size

        def fuel_type(self):
         return "Electric charge"

# my_tesla = ElectricCar("tesla", "MOdel S", "85kWh")
# print(isinstance(my_tesla,car))
# print(isinstance(my_tesla,ElectricCar))


# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())


# my_car = car("Tata", "Safari")
# # my_car.model = "City"
# car("tata", "nexon")

# # print(safari.general_description())
# print(my_car.model())


# print(safari.fuel_type())
# print(car.total_car)


# my_car = car("toyota", "Corolla") 
# print(my_car.brand)
# print(my_car.model)

# my_new_car = car("tata", "safari")
# print(my_new_car.model)
# print(my_new_car.brand)
# print(my_new_car.full_name())


# static method--> Add a static methos to the car class that returns 

class battery:
    def battery_info(self):
        return "this is battery"

class engiene:
    def engiene_info(self):
        return "this is engiene"

class ElectricCarTwo(battery, engiene, car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "model s")
print(my_new_tesla.engiene_info())
print(my_new_tesla.battery_info())
