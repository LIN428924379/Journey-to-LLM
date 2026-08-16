"""
    该案例演示了多分支
"""
from random import randint
price = 50
balance = randint(1, 100)
print(f"当前余额：{balance}")
if balance < price:
    print("余额不足，请充值")
else:
    print("消费成功")

print("欢迎下次光临")