'=============comperhensions============'

#генератор с помощью которого можно создать последовательность используя цикл for 
#for в одну строку

#range()
#{}
#[]
#{:}


#результат for элемент in последовательность


# list_1=[x+2 for x in [23,0,5,10]]#
# print(list_1)

list1=list()
# def new_func(list1):
#     for i in range(1,11):
#         if i%2==0:
#             list1.append(i)
#     print(list1)

#     list1=['четный' if i%2==0 else 'нечетный' for i in range(1,11) ]
#     print(list1)

# new_func(list1)


'В CONPREHANSIONS МОЖНО ДОБАВЛЯТЬ УСЛОВИЯ,ТАМ ИХ ДВА ВИДА'

'1-ТЕРНАРНЫЙ ОПЕРАТОР,ПИШЕТСЯ ПЕРЕД ЦИКЛОМ,ТАК КАК ИСПОЛЬЗУЕТСЯ IF ELSE'

"2-ФИЛЬТР ПИШЕТ ПОСЛЕ ЦИКЛА"



'==============виды comprehansion============='
'1-list'
'2-dict'
'3-set'


'Dictionary comprehansion'
dict1={i:i for i in range(1,11)}
print(dict1)



"Set comprehansions"
set1={i for i in range(1,11)}
print(set1)





