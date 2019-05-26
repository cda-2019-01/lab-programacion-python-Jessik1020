##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
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

for c in file:
	for key in c[3]:
		if key in count:
			count[key] += int(c[1])
		else:
			count[key] = int(c[1])


for key in sorted(count.keys()):
     print(key + ',' + str(count[key]))
