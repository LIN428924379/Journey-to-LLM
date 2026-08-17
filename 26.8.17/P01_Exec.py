# 编写一个 Python 程序，获取用户输入的整数，判断它是正数、负数还是零，并输出相应的结果
"""
num = int(input("请输入一个整数: "))
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("0")
"""

# 模拟用户登录验证，获取键盘上的输入，如果用户名root,密码是123456，提示登录成功，否则提示登录失败
"""
username = input("请输入用户名：")
password = input("请输入密码：")
if username == "root" and password == "123456":
    print("登录成功")
else:
    print("登录失败")
"""

# 从键盘上输入3位正整数，判断是否为水仙花数，水仙花数:3位正整数等于各个位数字的立方和
"""
num = input("请输入一个3位正整数：")
ans = 0
for i in num:
    ans += int(i) ** 3
if ans == int(num):
    print("该数字为水仙花数")
else:
    print("该数字不是水仙花数")
"""
"""
num = int(input("请输入一个3位正整数："))
a = num % 10
b = num // 10 % 10
c = num // 100
if num == a**3 + b**3 + c**3:
    print("该数字为水仙花数")
else:
    print("该数字不是水仙花数")
"""
