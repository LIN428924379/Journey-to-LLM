"""
    该案例演示了单分支
    商品价格50，小于50“余额不足，请充值”，最后打印“欢迎下次光临”
"""
from random import randint
price = 50
balance = randint(1, 100)
print(f"余额是{balance}")

if balance < price:
    print("余额不足，请充值")

print("欢迎下次光临")