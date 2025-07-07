# 变量，字符串， 函数调用
message = "hello python world"
print(message.title()) # python2.7 的print 不需要用小括号，用了是其他含义
print(message.upper())
print(message.lower())

# 字符串拼接
first_name = "Mark"
last_name = "Wu"
message = "Hello, " + first_name + " " + last_name
print(message)

# \n \t
print("\tpython")
print("hello\npython")
print("language:\n\tpython\n\tgo\n\tcpp")

# strip
hello_world = " hello world "
hello_world = hello_world.strip()
print(' python '.rstrip() + "End")
print(' python '.lstrip() + "End")
print(' python '.strip() + "End")
print(hello_world)

# number
print("2 + 3 = ", 2 + 3)
print("3 - 2 = ", 3 - 2)
print("3 * 2 = ", 3 * 2)
print("3 / 2 = ", 3 / 2) # python 2.7 是地板除
print("3 ** 2 = ", 3 ** 2)
print("3 ** 3 = ", 3 ** 3)
print("2 + 3*4 = ", 2 + 3*4)
print("(2 + 3)*4 = ", (2 + 3)*4)

# 浮点数
print("0.1 + 0.1 = ", 0.1 + 0.1)
print("0.2 + 0.2 = ", 0.2 + 0.2)

# str()
age = 32
print("happy " + str(age) + "rd Birthday")

# 终端输入 import this 查看python编程原则