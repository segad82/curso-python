set_a = {'col', 'mex', 'clp'}
set_b = {'pe', 'mex', 'br'}

#Podemos unir conjuntos, repetando la regla de NO elementos duplicados.
set_c = set_a.union(set_b)
print(set_c) # {'pe', 'mex', 'clp', 'br', 'col'}
#Podemos hacer la misma unión, pero con operador.
print(set_a | set_b) # {'pe', 'mex', 'clp', 'col', 'br'}

#Podemos hacer una intersección de conjuntos.
set_c = set_a.intersection(set_b)
print(set_c) # {'mex'}
#Podemos hacer la intersección con operador.
print(set_a & set_b) # {'mex'}

#Podemos hacer una diferencia de conjuntos.
set_c = set_a.difference(set_b)
print(set_c) # {'col', 'clp'}
#Podemos hacer la diferencia con operador.
print(set_a - set_b) # {'col', 'clp'}

#Podemos hacer una diferencia simétrica de conjuntos (excluye los elementos en intersección).
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'br', 'clp', 'pe', 'col'}
#Podemos hacer la diferencia simétrica con operador.
print(set_a ^ set_b) # {'pe', 'clp', 'br', 'col'} 