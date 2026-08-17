"""
    该案例演示了while循环
    第 1 周有 2 只兔子，此后每周兔子的数量都增加上周数量的 2 倍，且期间没有兔子死亡，求第 10 周共有多少只兔子：
"""
import time
"""
rabbit = 2
week = 1

while week < 10:
    rabbit += rabbit * 2
    week += 1

print(f"第{week}周共有{rabbit}只兔子")
"""
"""
# 打印进度条
num = 1
while num <= 100:
    print("=",end='')
    num += 1
    time.sleep(0.1)

"""
# while....else
rabbit = 2
week = 1

while week < 10:
    rabbit += rabbit * 2
    week += 1
else:
    print(f"第{week}周共有{rabbit}只兔子")
