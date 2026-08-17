"""
    给定月份，求该月有多少天
"""
from random import randint

month = randint(1, 12)
print(f"当前月份是：{month}")

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("当月有31天")
    case 4 | 6 | 9 | 11:
        print("当月有30天")
    case 2:
        print("当月有28或29天")