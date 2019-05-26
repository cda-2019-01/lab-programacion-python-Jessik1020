##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
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
	x = 0
	for d in c[4]:
		x += int(d.split(':')[1])
	print(c[0] + ',' + str(x))
