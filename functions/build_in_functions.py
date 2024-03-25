'==============Втроенные функции==============='
#map,filter,zip,enumerate,reduce

'ZIP'
 #cоединяет несколько последовательностей(получаем генератор,в катором элементы tuple)

list1=[1,2,3,4]
list2=['a','b','c']
list3=[10.5,20.6,35.8,0.5]
zipped=zip(list1,list2)
#print(list(zipped)) [tuple,tuple,tuple]
#print(dict(zipped)) {list1:list2,list1:list2}


'ENUMERATE'
#нумерует последовательность(по дефолту 0)(тоже возвращает генератор)

# enumerated=enumerate('hello')
# # print(list(enumerated))
#[(-100, 'h'), (-99, 'e'), (-98, 'l'), (-97, 'l'), (-96, 'o')]

# for i in enumerated:
    # print(i)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')


# enum=enumerate([12,8,'hi',True,'HELLO',None])
# # print(list(enum))
# # for i in enum:
# #     print(i)

# for n,v in enum:
#     print(f'номер:{n}, значение {v}')

'MAP'
#принимает другую функцию и последовательнрсть,МЭП ПРИМЕНЯЕТ функцию,которую передали на каждый элемент из последовательности.Возвращает map генератор


# list_=[1,2,3,4]
# def func(a):
#     return str(a)

# mapper=map(func,list_)


# print(mapper)#<map object at 0x793291b5bc40>
# print(list(mapper))#['1', '2', '3', '4']


# list_1=[1,2,3,4]
# def func(a):
#     return a**2
# mapper=map(func,list_1)
# print(list(mapper))


' lambda -  это однаразовая анонимная функция'


# result=lambda num1:num1**3
# print(result(2))

# list_=[1,2,3,4]
# def func(a):
#     return str(a)

# mapper=map(func,list_)

list_1=[1,2,3,4]
mapper=map(lambda a:a**2,list_1)


'FILTER'
#принимает другую функцию и последовательность, принименяет функцию которую мы передали на каждый элемент последовательности и оставляет только те элементы,которые прошли проверку


# list_=[-10,0,39,-12,-3,23,1,0]


# def func(a):
#     return a>=0

# filtered=filter(func,list_)
# print(list(filtered))
# filtered=filter(lambda a:a>=0,list_1)


# list_=[1,2,3,4,5,6,7,8]
# filtered=filter(lambda a:a%2==0,list_)
# print(list(filtered))




'REDUCE'
#принимает функцию и последователбность,возвращает 1 результат(передавая функция,должна принимать 2 аргумента)
from functools import reduce
list_1=[12,3,0,5]
reduced=reduce(lambda a,b:a+b,list_1)
print(reduced)



students = [
    {'student': 'Jack', 'marks': 43},
    {'student': 'Tom', 'marks': 92},
    {'student': 'Helen', 'marks': 85},
    {'student': 'Peter', 'marks': 58},
    {'student': 'Jessica', 'marks': 75}
]

sorted_students = sorted(students, key=lambda x: x['marks'], reverse=True)
print(sorted_students)




















