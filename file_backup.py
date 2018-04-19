#1.获取要复制的文件名
old_file_name = input("请输入要复制的文件名：")

#2。打开要复制的文件
f = open(old_file_name,"r")

#new_file_name = old_file_name+"备份"
position = old_file_name.rfind('.')
new_file_name = old_file_name[:position]+'备份'+ old_file_name[position:]
#3.创建新的文件
b = open(new_file_name,"w")
#4.将源文件内容复制到新文件中
inf = f.read()
b.write(inf)
#5.关闭两个文件
f.close()
b.close()
