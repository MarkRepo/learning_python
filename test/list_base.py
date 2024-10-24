# get
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])

# modify
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# append
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducta')
print(motorcycles)

# insert
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati")
print(motorcycles)

# del
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# pop
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

# pop(index)
motorcycles = ['honda', 'yamaha', 'suzuki']
poped_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(poped_motorcycle)

# remove (只删除第一个)
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove("honda")
print(motorcycles)

# sort (永久改变)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

# sorted (临时改变)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars, reverse=True))
print(cars)

# reverse
cars.reverse()
print(cars)

# len
print(len(cars))
