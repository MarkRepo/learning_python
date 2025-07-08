from car import Car  # 导入类
from electric_car import ElectricCar
from car import * # 导入所有类，不推荐
import car # 导入整个模块

my_new_car = Car('audi', 'a4', 2016)
my_new_car = car.Car('audi', 'a4', 2016) # module_name.class_name
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(46)
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
