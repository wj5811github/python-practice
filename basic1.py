import time

# # 学习PYTHON语言第一句话
# print("hello,world!")
# # 与print命令对应的是input
# input("请输入第一个数字：")
# # 定义一个变量并赋值
# num1 = 10
# num2 = 20
# result = num1 + num2
# print(result)
# # 使用time模块的sleep函数让程序暂停3秒
# time.sleep(3)
# # 新建一个列表
list1 = [1, 2, 3, 4, 5]
list2 = [11, 22, 33, 44, 55]
# 添加一个元素
list1.append(6)
# 合并两个列表
list1 = list1 + list2
print(list1)
# 追加一个列表
list1.extend(list2)  #extend函数没有返回值即返回值为NONE，所以不能用变量接收
print(list1)
# 从列表中删除一个元素，并用一个变量来接受删除的元素
pop_a = list2.pop()
print(pop_a)
# 新建一个元组
tuple_a = (111, 222, 333, 444, 555)
# 列表合并元组
list1.extend(tuple_a)
# 或者
list1 = list1 + list(tuple_a)
print(list1)

for i in range(10):
    print(f"{i}\t",end='')

print()
list_a = []
for i in range(20):
    if i % 2 == 0:
        list_a.append(i)
    else:
        pass
print(list_a)

# while循环案例1-九九乘法表：
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j * i}\t",end="")
        j += 1
    print()
    i += 1
print("\n----------#######----------")
# for循环案例2-九九乘法表：
for i in range(10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j * i}\t", end=" ")
    print()

list_b = [a for a in range(10)]  # 这种写法没见过呢 list可以  元组不行呢
print(list_b)

list_c = [b for b in range(10)]
print(list_c)