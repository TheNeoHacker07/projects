'===================функции==================='



#функции именнованное блок кода которыйм может принимать аргументы и возвращать результат



# def my_sum(x,y):#параметры
#     return x+y
# res=my_sum(5,10)# 5,10 аргументы



# def func(x):
#     print(x)


# func(input())

# def hello():
#     print('hekk')
# hello()


def my_len(a):
    count=0
    for i in a:
        count=count+1
    return count
my_len([2,4,5,2,1])

"функции соблюдвет принуциап DRY"

#параметры переменные внутри функциии,параметры мы создаем когда вызываем функцию
#аргументы -занчени которые мы передаем при вызове функции


def func(a,b):
    print(a,b)

func(10,3)


'===================виды параметров=========================='

#1.обезательные
#2 не обезательные
#  2.1 c дефолтом
#  2.2 args (со значением по умолчанию которые не попали в обязательные и с дефолтом)
# 2.3 kwargs(все лишние именннованные аргументы)


'=========================виды аргументов===================='

#позиционные(по позиции)
#именнованые(по названию(параметр=значение))

# def func(num1,num2):
#     print(num1+num2)
# func(10,20)


# def func(a,b*args,**kwargs):
#     print(a)
#     print(b)
#     print(*args)
#     print(**kwargs)






def div(a,b):
    if b==0:
         print('he')
    





