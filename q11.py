##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##

#Leer el archivo 
import glob #importar archivos
filenames=glob.glob('data.csv')

text =[] #Grabar archivo en una variable
for filename in filenames:
    with open(filename, 'rt') as f:
        text += f.readlines()

archivo2 = [row[0:-1] for row in text] #Eliminar retornos de carros
archivo2 = [row.split('\t') for row in archivo2] #Separar archivo en tab

#Respuesta
file = [] 
i = 0
for e in archivo2:
	file.append([])
	for f in e:
		a = f.split(',')
		if(len(a) == 1):
			file[i].append(a[0])
		else:
			file[i].append(a)
	i += 1
    
for c in file:
	print(c[0] + ',' + str(len(c[3])) + ',' + str(len(c[4])))
