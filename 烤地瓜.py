class SweetPatto:
    def __init__(self):
        self.cooked_Level = 0
        self.cooked_string = '生地瓜'
    def __str__(self):
        return '地瓜经过%d分钟的烘烤，已经是%s' %(self.cooked_Level,self.cooked_string)  
    def cook(self,cooked_time):
        self.cooked_Level += cooked_time
        if self.cooked_Level >=0 and self.cooked_Level <=3:
            self.cooked_string ="生地瓜" 
        elif self.cooked_Level >=3 and self.cooked_Level <=5:
            self.cooked_string ="半生不熟"
        elif self.cooked_Level >=5 and self.cooked_Level <=7:
            self.cooked_string ="熟了"
        elif self.cooked_Level >=7:
            self.cooked_string ="糊了"

#创建了一个对象
di_gua = SweetPatto()
print(di_gua)
di_gua.cook(2)
print(di_gua)
di_gua.cook(2)
print(di_gua)
di_gua.cook(2)
print(di_gua)
di_gua.cook(2)
print(di_gua)
