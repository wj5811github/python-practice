def func_a():
    print("可以打印出来1")
    return [1, 2, 3 ,4 ,5]

func_a() # 在被其它模块引用时会执行

if __name__ == '__main__':
    print(f"__name__的值为：{__name__}")
    print(func_a())