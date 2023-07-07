
money = 0

name = input("请输入您的姓名：")

def query(flag):
    if flag:
        print("-"*20,"欢迎光临","-"*20)
    print(f"尊敬的{name},您的帐户现有余额为：{money}元")
def cunqian():
    global  money
    zj = int(input("请输入存钱金额："))
    money += zj
    query(False)

def quqian():
    global  money
    qq = int(input("请输入取钱金额："))
    if qq <= money:
        money -= qq
        query(False)
    else:
        print("余额不足")

def main():

    print("查询请按1")
    print("存款请按2")
    print("取款请按3")
    print("退出请按4")

    keynum = input("请输入你的选择：")
    if keynum == "1":
        query(True)

    if keynum == "2":
        cunqian()

    if keynum == "3":
        quqian()

    if keynum == "4":
        print("谢谢光临，下次再见！\n退出程序了")

    return input("请输入你的选择：")

if __name__ == '__main__':
    main()
