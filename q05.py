##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
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
count = {}

for e in archivo2:
	count[e[0]] = []

for e in archivo2:
	count[e[0]].append(int(e[1]))

for key in sorted(count.keys()):  
     print(key + ',' + str(max(count[key])) + ',' + str(min(count[key])))
