#coding=utf-8
def test(a,b,func):
    result = func_new(a,b)
    print(result)
func_new = input("请输入匿名函数：")
func_new = eval(func_new)
test(11,22,func_new)
