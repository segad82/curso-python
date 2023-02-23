for i in range(1,11):
    print(i)
'''
1
2
3
4
5
6
7
8
9
10
'''

#Se puede iterar manualmente un elemento range, de la siguiente manera.
my_iterable = iter(range(1,4))
print(my_iterable) # <range_iterator object at 0x000001775E980BB0>
print(next(my_iterable)) # 1
print(next(my_iterable)) # 2
print(next(my_iterable)) # 3
#Al iterar más allá del límite del iterador, python genera una exepción.
print(next(my_iterable)) # StopIteration