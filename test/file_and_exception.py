# 读取整个file
# r 避免转义
file_path=r'.\test\pi_digits.txt'

# with 在不再需要访问文件后将其关闭
print("---- read ----")
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
print("---- for ----")
with open(file_path) as file_object:
    for line in file_object:
        print(line)

# 创建一个包含文件内各行内容的列表
print("---- readlines ----")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print("---- print pi ----")
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(float(pi_string))

# 写入文件
filename = 'prog.txt'
# open 默认是只读模式，r+ 表示读写，w写，a追加写
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# a 模式
with open(filename, 'a') as file_object:
    file_object.write("I also love find meaning in larget datasets.\n")
    file_object.write("I love creating apps that can run a browser.\n")

# exception: try-except-else
# ZeroDivisionError, FileNotFoundError
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't devide by zero!")
else:
    print("OK")

def count_words(filepath):
    try:
        with open(filepath) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(filepath + " Not found")
        # pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filepath + " has about " + str(num_words) + " words.")
        print(words)
filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
for filename in filenames:
    count_words(filename)

# Json dump and load
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = "numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    nums = json.load(f_obj)
print(nums)

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_user_name():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w')  as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_user_name()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
