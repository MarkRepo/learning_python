# 遍历
# for
print("-------------------for-------------------")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!')
print('Thank you, everyone. That was a great magic show!')

#注意缩进的误用

#创建数值列表
# range 1 2 3 4
print("-------------------range-------------------")
for value in range(1, 5):
    print(value)
numbers = list(range(1, 6))
print(numbers)

# list(), 步长
print("-------------------range step-------------------")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# min, max, sum
print("-------------------min,max,sum-------------------")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

#列表解析
print("-------------------list expr-------------------")
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 切片
print("-------------------list slice-------------------")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
for player in players[:3]:
    print(player.title())

# 赋值列表(两个独立的列表)
print("-------------------list slice for copy-------------------")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice_cream')
print(my_foods)
print(friend_foods)
# 引用列表(同一个列表)
print("-------------------list slice ref-------------------")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice_cream')
print(my_foods)
print(friend_foods)

# 元组 (不可变的列表)
print("-------------------tuple-------------------")
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历元组
print("-------------------tuple for-------------------")
for dimension in dimensions:
    print(dimension)

# 重新赋值是ok的
print("-------------------tuple reset-------------------")
dimensions = (400, 100) 
for dimension in dimensions:
    print(dimension)

# 设置代码格式(pep 8代码规范)：缩进（注意要把制表符转为空格），行长，空行
