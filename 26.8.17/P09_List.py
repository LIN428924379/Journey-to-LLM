"""
    该案例演示了列表
"""
"""
# 创建列表对象
list1 = [100, 200, 300, 400, 500]
print(list1, type(list1))

# 访问列表元素
print(list1[2])
print(list1[-3])

# 切片
print(list1[1:4])
print(list1[1:4:2])
print(list1[::-1])

list1.reverse()
print(list1)

list2 = list1
print(id(list1), id(list2))
list2 = list1[:]
print(id(list1), id(list2))
"""
"""
list1 = [100, 200, 300, 400, 500]

# 向列表中添加元素
# list1.append(600)
# print(list1)

list1.insert(2, 600)
print(list1)
"""
"""
# 列表相加
list1 = [1,2,3]
list2 = ["a", "b", "c"]
print(list1+list2)
"""
"""
# 列表乘法
list1 = [100, 200, 300, 400, 500]
print(list1 * 2)
print(list1)
"""
"""
# 修改列表中的元素
list1 = [100, 200, 300, 400, 500]
list1[2] = 30
print(list1)
list1[1:4] = ["a", "b", "c"]
print(list1)
# 判断元素是否在列表中
print(100 in list1)
"""
"""
# 获取列表中的元素的个数
list1 = [100, 200, 300, 400, 500]
print(len(list1))
# 最大值，最小值，求和
print(max(list1))
print(min(list1))
print(sum(list1))
"""
"""
# 遍历列表中的元素
list1 = [100, 200, 300, 400, 500]

# 直接遍历
for i in list1:
    print(i)

print('-'*30)

# 下标遍历
for i in range(len(list1)):
    print(list1[i])

print('-'*30)

# 同时拿到下标和值
for i, v in enumerate(list1):
    print(i, v)
"""
"""
# 删除列表中的元素
# 删除指定元素
# list1 = [100, 200, 300, 400, 500]
# list1.remove(300)
# print(list1)
# 删除指定位置元素
# del list1[0]
# print(list1)
# del list1
# print(list1)

list1 = [100, 200, 300, 300, 300, 400, 500]
for item in list1[:]:
    if item == 300:
        list1.remove(item)

print(list1)
"""
"""
# 列表嵌套
list1 = [[1,2],[3,4],[5,6]]
# print(type(list1))

for item in list1:
    for i in item:
        print(i)
"""
"""
# 列表推导式
# list1 = [1,2,3,4,5]
# list2 = [i*2 for i in list1]
# print(list1)
# print(list2)

# list2 = [i*2 for i in range(10) if i % 2 == 0 ]
# print(list2)

# list3 = [100,200,300,300,300,400,500]
# list4 = [i for i in list3 if i != 300]
# print(list3)
# print(list4)

# list5 = [1,2,3,4,5]
# list6 = ["a","b","c","d","e"]
#
# list7 = [(i,j) for i in list5 for j in list6]
# print(list7)

list5 = [1,2,3,4,5]
list6 = ["a","b","c","d","e"]
zipped = zip(list5, list6)
print(list(zipped))
"""
