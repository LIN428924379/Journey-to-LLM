"""
    该案例演示了变量
"""
"""
num1 = 5
num2 = 10
num3 = num1 + num2

print(num1)
print(num2)
print(num3)

name = "zs"
age = 20
weight = 80.5

# 同时创建多个变量
# 多个变量值相同
var1 = var2 = var3 = 20
print(var1, var2, var3)
# 多个变量值不同
a = 10
b = 20
c = 30
a1, b1, c1 = 10, 20, 30
print(a, b, c)
print(a1, b1, c1)

# 变量修改
num1 = 20
num1 = 50
print(num1)

# 交换两个变量的值
a = 10
b = 20
print(a,b)
a,b = b,a
print(a,b)
"""
# 不同进制的表示
dec_num = 10
binary_num = 0b1010
oct_num = 0o12
hex_num = 0xA

print(dec_num, binary_num, oct_num, hex_num)
print(bin(dec_num))
print(oct(dec_num))
print(hex(dec_num))