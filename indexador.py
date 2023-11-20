import pandas as pd
import matplotlib as mpl

mpl.style.use('bmh')

### Leo el archivo original y le cambio el indice ###
dfpre = pd.read_csv('precios18.csv',sep = ',')
indice = dfpre['Time']
columnas = dfpre.columns[1:]
valores = dfpre.values[:,1:]
df = pd.DataFrame(valores, index = indice, columns = columnas)


###********* Escritura de archivos ************#
archivo_csv = 'flores18.csv'
#dfjoya.to_csv(archivo_csv)#, index = False)
#with open(archivo_csv, mode='w') as archivo:
    #writer = csv.writer(archivo)//Creo que anda bien esto
    #writer.writerrows(dfjoya)
#print(f"El archivo flores.csv ha sido creado con exito")