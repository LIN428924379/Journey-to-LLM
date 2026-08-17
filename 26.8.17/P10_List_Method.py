"""
    该案例演示了list中的函数
"""
list1 = [100, 200, 300, 400, 500]
# list.insert(index,x) 在指定位置插入 x
# list1.insert(0,30)
# list.append(x) 在列表末尾追加 x
# list1.append(600)
# print(list1)
# list1.extend(list2) 在列表 1 的末尾追加列表 2 的数据
# list1.extend([600])
# del list[index] 删除指定位置的数据或切片
# del list1[0:3]
# list.remove(x) 删除第一次出现的 x
# list1.remove(200)
# list.pop([index]) 删除指定位置的数据，默认为末尾数据
# list1.pop()
# list.clear() 清空列表中元素
# list1.clear()
# list[index] = x 修改指定位置的数据
# list1[1] = 555
# list1[start:end] = list2 修改列表切片的数据
# list1[0:3] = [11,22,33]
# sorted(list[,reverse=True]) 返回排序后的新列表，可选降序
# print(sorted(list1))
# list.sort([reverse=True]) 对列表就地排序，可选降序
# list1.sort()
# print(list1)
# list.reverse() 反转列表中的元素
# list1.reverse()
# print(list1)
# list.index(x[,start,[,end]]) 返回 x 在列表中首次出现的位置，可指定起始和结束范围
# print(list1.index(200))
# list.count(x) 返回 x 的数量
# print(list1.count(100))
# len(list) 返回列表元素个数
# print(len(list1))
# max(list) 返回列表中最大值
# print(max(list1))
# min(list) 返回列表中最小值
# print(min(list1))
# sum(list) 返回列表中所有元素和
# print(sum(list1))
# list.copy() 拷贝列表
# list2 = list1.copy()
# print(list1, list2)
# print(id(list1), id(list2))
# list(x) 将序列转换为列表
# str1 = "Hello World"
# print(list(str1))