"=======================Области видимости================="
#LEGB -  local enclosed global build in

'build in встроенная пространство)'
#это пространство которое находится в python(int,str,input,print,sum)

'Global(глобальное пространство)'
#Это пространство которое находится у вас файле
#globals() показыввает все глобальные переменные

# a=5
# b='hello'
# print(globals())


# 'Enclosed(замкнутое)'
# #Это пространство которое находится во вложенных функциях
# var='global'
# def func():
#     #локальное простраство для глобального пространство
#     var='encolsed'
#     #замкнутое пространство (потому что есть более замкнутое)
#     def func2():
#         #локальное пространство для пространства func
#         var='local'
#         print(var)
#     print(var)
#     func2()


# print(var)
# func()


'local(Локальное пространство)'
#Это пространство которое находится внутри функции
#locals выводит переменные локального пространства

# a=10

# def func3(a,b):
#     print(a,b)
#     print('глобальное',globals())
#     print('локалное',locals())

# func3(0,1)

# var='global'

#global  это оператор который позволяет менять перемнную с глобального пространства
# def func():
#     global var
#     var=10
#     print(var)

# print(var)

# func()
# print(var)



# def func():
#     var='enclosed'
#     def func2():
#         nonlocal var
#         var=10
#         print(var)

#     func2()



# func()


'nonlocal-это оператор,который позволяет менять переменнную с не локальногоп пространства'


count=0
def func():
    global count
    count+=1










