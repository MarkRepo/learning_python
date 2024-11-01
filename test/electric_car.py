from car import Car

# 继承, 组合
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    # 重写父类方法
    def fill_gas_tank(self):
        print("This car doesn't need a gs tank!")

# python2.7 的继承
# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super(ElectricCar, self).__init__(make, model, year)