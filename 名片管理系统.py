#用来存储名片
card_infors = []   #全局变量

def print_menu():
    '''完成打印功能菜单'''
    print("="*30)
    print("名片管理系统 v1.3.5")
    print("1.添加一个新的名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有名片")
    print("6.退出系统")
    print("="*30)

def add_new_card_infor():
    '''添加新的名片'''
    new_name = input("请输入新的名字：")
    new_phoNum =input("请输入新的手机号码：")
    new_weixin = input("请输入新的微信号码：")
    new_addr = input("请输入新的住址：")

    #定义新的字典，来存储新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['phoNum'] = new_phoNum
    new_infor['weixin'] = new_weixin
    new_infor['addr'] = new_addr

    #将一个字典添加到列表中去
    card_infors.append(new_infor)

def del_card_infor():
    '''删除名片'''
    pass

def change_card_infor():
    '''修改名片信息'''
    pass

def find_card_infor():
    '''查询名片信息'''
    find_name = input("请输入您要查询的姓名：")
    find_flag = 0 #默认没找到
    for temp in card_infors:
        if find_name == temp['name']:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['phoNum'],temp['weixin'],temp['addr']))
            find_flag=1#表示找到了
            break

        #判断是否找到了
    if find_flag == 0:
        pritn("查无此人")

def print_card_infor():
    '''显示所有名片'''
    pass
'''
def exit_card_infor_sys():
     退出系统
     pass
     '''
#1 打印功能提示
print_menu()


while   True:
    #获取用户是操作
    num = int(input("请输入操作所对应的序号："))
    
    #进行相应的操作
    if num==1:
        add_new_card_infor()

    elif num==2:
        del_card_infor()

    elif num==3:
        change_card_infor()

    elif num==4:
        find_card_infor()

    elif num==5:
        print_card_infor()

    elif num==6:
       # exit_card_infor_sys()
        break
    else :
        print("输入有误，请重新输入")
