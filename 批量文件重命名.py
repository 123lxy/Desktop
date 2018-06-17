import os
#1.获取要改名的文件夹
folder = input("请输入要操作的文件夹名：")
#2.列出文件夹所有文件
file_names = os.listdir(folder)
print(file_names)
#3.批量重命名
#os.chdir(folder)
'''
    old_name = name
    new_name = '[百度云]' + name
    os.rename(old_name,new_name)
    print(new_name)
'''
for name in file_names:    
    old_name ='./'+folder+'/'+name 
    new_name ='./'+folder+'/'+'[百度云]' + name
    os.rename(old_name,new_name)
    print(new_name)

