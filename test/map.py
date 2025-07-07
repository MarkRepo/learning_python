# 访问map
from math import pi

print('-----------------map visit------------------')
alien_0 = {"color": 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# add key-value
print('-----------------map add------------------')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# update
print('-----------------map update------------------')
alien_0['color'] = 'yellow'
print(alien_0)

# del
print('-----------------map del------------------')
del alien_0['points']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# 多行打印
print("Sara's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

print('-----------------map for------------------')
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# 遍历
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 遍历key, 没有keys调用，默认也是遍历key
# sorted 排序
print('-----------------map key sort------------------')
for name in sorted(favorite_languages.keys()):
    print(name.title())

# set 去重
print('-----------------map value uniq------------------')
for language in set(favorite_languages.values()):
    print(language.title())

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')

# 字典列表
print('-----------------map list------------------')
alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15} 
aliens = [alien_0, alien_1, alien_2]
print(aliens)

print('-----------------map list2------------------')
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("Total number of aliens: " + str(len(aliens)))

# 字典中存放列表
print('-----------------map list value------------------')
pizza = {
    'crust': "thick",
    'toppings': ['mushrooms', 'extra cheese'],
}
print(pizza)

# 字典中存字典
print('-----------------map map------------------')
users = { 
    'aeinstein': {
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton', 
    }, 
    'mcurie': { 
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
    }, 
 }
print(users)