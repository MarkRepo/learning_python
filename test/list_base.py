# get
print("-------------------get-------------------")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

# modify
print("-------------------modify-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# append
print("-------------------append-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducta')
print(motorcycles)

# insert
print("-------------------insert-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)

# del
print("-------------------del-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# pop
print("-------------------pop-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

# pop(index)
print("-------------------pop(index)-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(poped_motorcycle)

# remove (只删除第一个)
print("-------------------remove-------------------")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove("honda")
print(motorcycles)

# sort (永久改变)
print("-------------------sort-------------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

# sorted (临时改变)
print("-------------------sorted-------------------")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))
print(cars)

# reverse
print("-------------------reverse-------------------")
cars.reverse()
print(cars)

# len
print("-------------------len-------------------")
print(len(cars))
