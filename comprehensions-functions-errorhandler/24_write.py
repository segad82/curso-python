'''
[x] : Crear - Crea el archivo especificado, devuelve un error si el archivo existe. | puntero al inicio
[r] : Lectura - Valor predeterminado. Abre un archivo para lectura, error si el archivo no existe. | puntero al inicio
[r+]: Lectura y escritura - Abre un archivo para lectura y escritura, error si el archivo no existe. | puntero al inicio
[w] : Escribir - Abre un archivo para escribir, crea el archivo si no existe. (Ojo! elimina contenido del archivo actual) | puntero al inicio
[a] : Agregar - Abre un archivo para agregar, crea el archivo si no existe. | puntero al final

Además, puede especificar si el archivo debe manejarse como modo binario o de texto.

[t] - Texto - Valor por defecto. Modo de texto.
[b] - Binario - Modo binario (por ejemplo, imágenes).
'''

with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
    file.write('\nnuevas cosas en este archivo')
    for i in range(0,6):
        file.write(f'line {str(i)}\n')