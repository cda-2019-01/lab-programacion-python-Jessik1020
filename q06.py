##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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
		count[x[0]] = []

for k in file:
	for l in k[4]:
		x = l.split(':')
		count[x[0]].append(int(x[1]))

# print result

for key in sorted(count.keys()):  
     print(key + ',' + str(min(count[key])) + ',' + str(max(count[key])))
