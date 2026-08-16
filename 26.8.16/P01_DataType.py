"""
    该案例演示了数据类型
"""
# 整数类型
# num1 = 10
# int1 = 1_000_000_000_000
# print(type(num1))
# print(int1)

'''
# 定于一个bool
num1 = True

# 定义整数
num2 = 20

print(type(num1))
print(type(num2))

print(type(num1)==type(num2))

print('-'*20)

print(isinstance(num1, bool))
print(isinstance(num2, int))
print(isinstance(num1, int))

# 小整数池  [-5,256]
num1 = 10
num2 = 10
num3 = 10

# id()
# print(id(num1), id(num2), id(num3))
num4 = 300
num5 = 300
print(id(num4),id(num5))

# 浮点数类型
f1 = 0.1
f2 = 0.2
print(type(f1))
print(type(f2))
f3 = f1 + f2
print(f3)

from decimal import Decimal
# 创建 Decimal 类型对象
f4 = Decimal('0.1')
f5 = Decimal('0.2')
print(type(f4),type(f5))
f6 = f4 + f5
print(f6)

# bool类型
b1 = True
b2 = False
print(type(b1))
print(type(b2))

# print(b1 == 1)
# print(b2 == 0)
# print(b1 + 10)

# 判断是否指向同一个地址
# print(b1 is 1)

b3 = True

print(id(b1),id(b3))
'''
# 字符串类型
# 单引号
# str1 = 'hello world'
# 双引号
# str1 = "hello world"
# print(str1)
# print(type(str1))

# 三引号
str1 = """
    hello world!
    hello python!
"""
print(str1)