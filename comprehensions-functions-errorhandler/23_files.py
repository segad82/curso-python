file = open('./text.txt') # Abre un archivo

print(file.readline()) # Lee una línea
print(file.readline()) # Lee la siguiente línea
print(file.readline()) # Lee la siguiente línea
print(file.readline()) # Lee la siguiente línea...

print(file.read()) # Lee un archivo completo o termina de leer todo lo pendiente

file.close() # Cierra el archivo para liberar memoria

print('*'*10)
'''
Cuando son archivo con poco contenido, el método 'read()' funciona bien.
Pero cuando son archivos con mucho contenido, es una buena práctica usar el método 'readline()'.
EL problema es que no sabemos cuando parar. ¿cómo solucionamos esto?
De la siguiente manera y lo bueno es que no abre el archivo completo, en cambio lo lee línea a línea.
'''
file = open('./text.txt')
for line in file:
    print(line)
file.close()

'''
Siembre que abramos un archivo, debemos recordar cerrarlo.
Existe una manera de trabajar con los archivos donde python los cierra automáticamente.
'''
with open('./text.txt') as file:
    for line in file:
        print(line)