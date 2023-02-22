#Existen los siguientes alcances a los que las variables se pueden definir.
# > Built-in
# >> Global scope
# >>> Enclosing scope
# >>>> Local scope
# ( ( ( (Local scope) Enclosing scope) Global scope) Built-in)

price = 100 # global
result = 200

def increment():
    price = 200 # local
    result = price + 10
    print(result) # 210
    return result

print(price) # 100
price_2 = increment()
print(price_2) # 210
print(result) # 200