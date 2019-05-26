
##
## Imprima la suma de la segunda columna.
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

suma = 0 #Respuesta 1
for f in archivo2:
    suma += int(f[1])
print(suma)

