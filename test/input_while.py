# input()
# python 2.7 使用raw_input() 获取输入，2.7也有input，input会把输入解读为python代码并执行
from timeit import repeat

print("-------------input-------------")
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# 提示超过一行时
print("-------------prompt multi lines-------------")
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

# int()
print("-------------input int-------------")
age = input("How old are you? ")
age = int(age)

# 求模
print( 4 % 3 == 1)
number = int(input("enter a number, and I'll tell you if it's even or odd: "))
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

# while input
print("-------------input while-------------")
prompt = "\nTell me something, and I will repeat it back to you:" 
prompt += "\nEnter 'quit' to end the program. " 
message = "" 
while message != 'quit': 
    message = input(prompt)
    if message != 'quit':
        print(message)

# 使用flag
print("-------------whle with flag-------------")
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# break
print("-------------whle with break-------------")
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# continue
print("-------------whle with continue-------------")
current_number = 0 
while current_number < 10: 
    current_number += 1 
    if current_number % 2 == 0: 
        continue 
    print(current_number)

# 使用while循环处理列表和字典
# 在列表之间移动元素
print("-------------whle with pop append-------------")
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除特定值的列表元素
print("-------------whle with remove-------------")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# 使用用户输入填充字典
print("-------------whle with map-------------")
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input('Would you like to leat another person respond?(yes/no)')
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")