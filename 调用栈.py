#调用栈
def greet(name):
    print('hello'+name+'!')
    greet2(name)
    print('haha'+name)
    bye()
def greet2(name):
    print(name+'is cool') 
def bye():   
    print('I love you')

greet('liu')
