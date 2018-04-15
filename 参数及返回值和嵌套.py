def sum_num(a,b,c):
    result1 = a+b+c
    #print("三个数总和为：%d+%d+%d=%d"%(a,b,c,result1))
    print("三个数总和为：%d"%result1)
    return result1
def average_num(result2):
    average_result = result2 /3
    print("总和平均数为：%d"%average_result)

num1 =int(input("请输入数字1："))
num2 =int(input("请输入数字2："))
num3 =int(input("请输入数字3："))
result1 = sum_num(num1,num2,num3)
average_num(result1)
