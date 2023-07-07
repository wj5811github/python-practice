from  basic2  import  func_a
# 当import一个模块后就会执行该模块的内容
# result = basic2.func_a() # 可以打印出来1
# print(f"result的类型为：{type(result)},值为：{result}")
print(f"__name__的值为：{func_a.__name__}")


words = []
with open("D:/vmware.txt", "r", encoding="utf-8") as f:

    for line in f:
        word = line.strip().split(" ")[2]
        words.append(word)
        print(words)
