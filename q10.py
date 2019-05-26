##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
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

count = {}

for k in file:
	for l in k[4]:
		x = l.split(':')
		count[x[0]] = 0

for k in file:
	for l in k[4]:
		x = l.split(':')
		count[x[0]] += 1

for c in sorted(count):  
     print(c + ',' + str(count[c]))
