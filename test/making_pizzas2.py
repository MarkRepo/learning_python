# 导入指定函数： from module_name import function_0, function_1, function_2
from pizza import *
from pizza import make_pizza
from pizza import make_pizza as mp
import pizza as p

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'grenn peppers', 'extra cheese')
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'grenn peppers', 'extra cheese')
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'grenn peppers', 'extra cheese')