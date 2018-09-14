#!usr/bin/env python
#encoding:utf-8
  
def find_Second_large_num(num_list):
    '''
    找出数组中第2大的数字
    '''
    #直接排序,输出倒数第二个数即可
    tmp_list=sorted(num_list)
    print 'Second_large_num is:', tmp_list[-2]
    #设置两个标志位一个存储最大数一个存储次大数
    #two存储次大值，one存储最大值，遍历一次数组即可，先判断是否大于one，若大于将one的
    #值给two，将num_list[i]的值给one；否则比较是否大于two，若大于直接将num_list[i]的
    #值给two；否则pass
    one=num_list[0]
    two=num_list[0]
    for i in range(1,len(num_list)):
        if num_list[i]>one:
            two=one
            one=num_list[i]
        elif num_list[i]>two:
                two=num_list[i]
        else:
            pass
    print ('Second_large_num is:', two)
 
 
if __name__ == '__main__':
    num_list=[11,12,44,33,52,57,89,32,1]
    find_Second_large_num(num_list)
