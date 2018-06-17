#计算n的阶乘
def num(x):
    if x==1:
        return 1
    else:
        return x*num(x-1)
    #@    print(result)
num(5)
