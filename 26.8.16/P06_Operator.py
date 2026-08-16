"""
    该案例演示了运算符
"""
'''
# 算术运算符
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 5)
print(10 % 5)
print(10 ** 5)

# 赋值运算符
a = 10
# a = a + 1
a += 1
print(a)
a -= 1
print(a)
a *= 2
print(a)
a /= 2
print(a)
a %= 2
print(a)
a **= 2
print(a)
a //= 2
print(a)

# 海象运算符 :=
num1 = 10
num2 = 20
print(num3 := num1 + num2)

# 比较运算符
num1 = 10
num2 = 20
print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

# 逻辑运算符
# x and y，x为False则返回x值，否则返回y值
b1 = False
b2 = True
# print(b1 and b2)
# print(b2 and b1)

# x or y，x为True则返回x的值，否则返回y值
x = 0
y = 8
print(x or y)

print(not x)

# 成员运算符
# list1 = [10, 20, 30]
# print(10 in list1)
# print(100 in list1)

# 身份运算符
num1 = 10
num2 = 1
# print(num1 == num2)
# print(num1 is num2)
b1 = True
print(num2 == b1)
print(num2 is  b1)
print(num2 is not b1)
'''
