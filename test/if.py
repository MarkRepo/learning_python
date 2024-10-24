# if 语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car == 'audi':
        print(car.lower())
    else:
        print(car.title())

# 条件测试, 相等 不等, and, or, >=, <=
car = 'Audi'
print(car == 'Audi')
print(car.lower() == 'audi')
print(car.lower() != 'Audi')
age = 18
print(age == 18)
print(age != 18)
print(age >= 18 and age <= 18)
print(age >= 18 or age <= 16)
 # in, not in
print('audi in cars: ', 'audi' in cars)
print('tesla not in cars: ', 'tesla' not in cars)

# if 检查列表是否为空
empty_list = []
if empty_list:
    print("not empty list")
else:
    print("empty list")