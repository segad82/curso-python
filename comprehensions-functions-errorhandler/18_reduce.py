import functools

numbers = [1,2,3,4]

def accum(counter, item):
    print('counter: ', counter)
    print('item: ', item)
    return counter + item
'''
counter:  1
item:  2 

counter:  3
item:  3   

counter:  6
item:  4  
'''

result = functools.reduce(accum, numbers)
print(result) # 10

result = functools.reduce(lambda counter, item : counter + item, numbers)
print(result) # 10