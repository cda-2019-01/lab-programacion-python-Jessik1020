##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
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
	count[(e[2].split('-')[1])] = 0

for e in archivo2:
	count[(e[2].split('-')[1])] = count[(e[2].split('-')[1])] + 1

for key in sorted(count.keys()):  
     print(key + ',' + str(count[key]))
