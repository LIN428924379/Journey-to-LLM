"""
    该案例演示了类型转换
"""
'''
# 相同类型运算，没有涉及类型转换
num1 = 10
num2 = 20
num3 = num1 + num2

print(type(num1))
print(num3)
print(type(num3))

# 自动类型转换(隐式转换)
num1 = 10
f1 = 5.0
res = num1 + f1
print(type(num1))
print(type(f1))
print(res)
print(type(res))

# 两个整数进行除法运算也是浮点型
num1 = 10
num2 = 2
num3 = num1 / num2

print(type(num1))
print(num3)
print(type(num3))

# 整数和字符串相加会报错
num1 = 10
str1 = "hello"
print(str1 + num1)
'''
# int(x [,base]) 将 x 转换为一个整数，x 若为字符串可用 base 指定进制
# res = int('10', 2)    # 2
# res = int('10', 8)      # 8
# print(res)
# float(x) 将 x 转换为一个浮点数
# print(float('12'))
# complex(real[,imag]) 创建一个实部为 real，虚部为 imag 的复数
# print(complex(3, 2))
# str(x) 将对象 x 转换为一个字符串
# print(str("hello \n world"))
# repr(x) 将对象 x 转换为一个字符串，可以转义字符串中的特殊字符
# print(repr("hello \n world"))
# eval(x) 执行 x 字符串表达式，并返回表达式的值
# eval("print(123)")
# bin(x) 将一个整数转换为一个二进制字符串
# print(bin(10))
# oct(x) 将一个整数转换为一个八进制字符串
# print(oct(10))
# hex(x) 将一个整数转换为一个十六进制字符串
# print(hex(10))
# ord(x) 将一个字符转换为它的 ASCII 整数值
# print(ord('a'))
# chr(x) 将一个整数转换为一个 Unicode 字符
# print(chr(97))
# tuple(s) 将序列 s 转换为一个元组
# list(s) 将序列 s 转换为一个列表
# set(s) 转换 s 为可变集合