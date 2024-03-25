

#range(start,end,step) это генератор которая генерирует/создает диапазон от start до end



# print(list(range(0,11,2)))#0,2,4,6,8,10


# print(list(range(0,10))) #1 2 3 4 5 6 7 8 9

# print(list(range(0,11,3)) )#0 3 6 9



# print(list(range(1,11,-1))) # 10  9 8 7 6 5 4 3 2 1





'==========методы списков============'


lidsr_1=[1,2,14,"hello",True,[0,0,0]]


lidsr_1[3]#hello
lidsr_1[-1] #[0,0,0]




#list(hello) h e l l o

list_2=list(range(0,101))# 1,2,3,4...100



#append добавление элемента в конец списка


list_=[]



list_.append(1)
list_.append('hello world')
list_.append(True)

# print(list_) #[1,hello world True]


'pop удаление списка элемета по индексу возвращает элемент если не указать индекс то удалит  с конца'

# list=[90,True,None,'hi']


# popped=list.pop(1)
# print(list)# hi none hi
# print(popped) #true




'remove это удаление элемента из списка по значению,'

# list_=[1,2,3,5,99,0,-11]
# list_.remove(5)

# list_.remove(True) #1
# #print(list_)



'count-считает количество элемента в списке '


# list_=[1,23,1,4,5,6,1,7,1,7,8,1,"hi","hi"]
# print(list_.count(1))#5
# print(list_.count(7))#2
# print(list_.count("hi"))#2


'index-метод находят индекс возвращает первого вхождения принятого элемента'
list_=['hi',1,"hi",341,2,0,'makers',2,1,99,10]

print(list_.index(0))#4
print(list_.index('makers'))#5







'extend расширяет список с помошью другого списка'

list1=[1,2,3]
list2=[0,0,0]

list1.append(list2) #[1,2,3,[0,0,0]]
list1.extend(list2) # [1,2,3,0,0,]


'reverse- изменяет список в обратном порядке'


list_=['hi',1,2,3,True,[1,2,3]]
list_.reverse()

print(list_)# [1,2,3] true 3 2 1 hi



'sort сортирует список состящий из одного типа данных'
list_=[12,4,1,0,25,7]


list_.sort(reverse=True)

print(list_)




list_=['c','b','a','A','B']

list_.sort(reverse=True)

print(list_)


"clear -очищает список"

list_=[12,42,1,'hi']

list_.clear()

a=10
b=5
c=2


a,b,c=10,5,2
print(a)



list=[23,'hi',4,0,'makers']


paket1=[
]
paket2=[]


meshok=['k','l','k','l','k']

















































