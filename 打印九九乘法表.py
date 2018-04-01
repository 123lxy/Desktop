i=1
while i<=9:   #用来控制行数

    j=1

    while j<=i:   #用来控制每一行中列数
        print("%d*%d=%d\t"%(j,i,j*i),end="")
        j+=1
    print("")

    i+=1

