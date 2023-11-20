import pandas as pd
import openpyxl as opn
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import datetime
import seaborn as sns
mpl.style.use('bmh')


### Declaracion de variables ###


### Leo el archivo original y le cambio el indice ###
dfpre = pd.read_csv('precios.csv',sep = ',')
indice = dfpre['Time']
#fecha_hora = datetime.datetime.fromtimestamp(indice)
columnas = dfpre.columns[1:]
valores = dfpre.values[:,1:]
dfjoya = pd.DataFrame(valores, index = indice, columns = columnas)
#dfjoya['fecha_hora']=datetime.datetime.fromtimestamp(indice)
#print(dfjoya.index[0])

### Constantes calculadas ###
temporalidad = ((dfjoya.index[2]-dfjoya.index[1])/60000).astype(int)
#print(temporalidad)

### Columnas calculadas ###
    ## Fecha y hora en formato legible ##
#for milis in dfjoya.index:
    #dfjoya['fech-h'] = datetime.datetime.fromtimestamp(milis/1000)

    ## Variación del precio [$]##
dfjoya['variacion'] = dfjoya['close'].astype(float)-dfjoya['open'].astype(float)

    ## Velocidad de variacion del precio [$/min] ##
dfjoya['velocidad'] = dfjoya['variacion']/temporalidad

    ## Velocidad de variacion de la velocidad [Vel/min] ##
dfjoya['aceleracion'] = dfjoya['velocidad']/temporalidad

    ## Fuerza Variacion del precio por el volumen ##
dfjoya['fuerza'] = dfjoya['variacion']*dfjoya['volume']

#print(dfjoya.head(3))
#print(dfjoya.describe)


###********* Escritura de archivos ************#
archivo_csv = 'flores.csv'
#dfjoya.to_csv(archivo_csv)#, index = False)
#with open(archivo_csv, mode='w') as archivo:
    #writer = csv.writer(archivo)//Creo que anda bien esto
    #writer.writerrows(dfjoya)
#print(f"El archivo flores.csv ha sido creado con exito")


###********* Pruebas graficas ************###
categorias = ['A','B','C']
valores = [20,10,15]

#plt.bar(dfpre['Time'],dfpre['close'].astype(float))
#plt.bar(dfjoya.index[2],dfpre['close'].astype(float))
#plt.bar(dfpre['close'].astype(float))
#plt.bar(categorias,valores)

fig, ax = plt.subplots()

#fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 8), sharex=True, sharey=False)

#ax[0].plot(dfjoya.index, dfjoya['close'], label='Precio', lw=1)
#ax[0]=sns.lineplot(data=dfjoya, x=dfjoya.index, y="close")
#ax[1]=sns.barplot(x=dfjoya.index, y="volume", data=dfjoya, color='red')
#ax[1].plot(dfjoya.index, dfjoya['volume'], label='Volumen', color='C1',lw=1)
#ax[2].plot(dfjoya.index, dfjoya['velocidad'], label='Velocidad', color='C2')

#ax[0].set_title('Precio y volumen') 
#ax[2].set_xlabel('Tiempo')  
#ax[1].set_ylabel('Precipitación (mm.)')


#ax[0].legend()  
#ax[1].legend()
#ax[2].legend()    


#ax.plot(dfpre['Time'],dfpre['close'], c='r', label = 'precio BTC',lw=1)

#sns.scatterplot(data=dfpre, x="Time", y="close", hue="species", ax=axs[0])

#ax.scatter(dfpre['Time'],dfpre['volume'], c='g', label = 'precio BTC', lw=0.5)#ANDA BIEN
#ax.scatter(dfjoya.index,dfjoya['volume'], c='g', label = 'Volumen BTC', lw=0.5)# ANDA BIEN, AGREGAR AL COLAB
#ax.bar(dfjoya.index,dfjoya['volume'], color='g')#label = 'precio BTC')
#ax.hist(dfjoya['close'],bins=20)#anda bien

#ax.set_xlabel('Tiempo')
#ax.set_ylabel('Precio')
#ax.set_title('Precio del bitcoin en funcion del tiempo')
#ax.bar
#ax.axhline(y=30000, color='r')
#ax.legend()
#plt.show()

ax.boxplot(dfjoya['volume'])# ANDA BIEN, HAY QUE DARLE FORMA

#------------------  Seaborn  -------------------#
#flights = sns.load_dataset("flights")
#print(flights.head(5))
#may_flights = flights.query("month == 'May'")
#sns.lineplot(data=dfjoya, x=dfjoya.index, y="close")#Anda bien agregar a COLAB

# Axis-level
#flights_wide = flights.pivot_table("year", "month", "passengers")
#flights_wide.head()
#sns.lineplot(data=flights_wide)

# Scatterplot
tips = sns.load_dataset("tips")
tips.head()
# Axis-level
#sns.scatterplot(data=dfjoya, x=dfjoya.index, y="close")Anda bien agregar a COALB pero con otra variable por ejemplo fuerza
# Axis-level
#sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")

# Barplot
#sns.set_theme(style="whitegrid")
#tips = sns.load_dataset("tips")
##flores = sns.load("flores.csv")
# Axis-level
#ax = sns.barplot(x="day", y="total_bill", data=tips)
#ax = sns.barplot(x=dfjoya.index, y="volume", data=dfjoya, color='red')# Anda OK. # ANDA BIEN, AGREGAR AL COLAB
#sns.histplot(data=dfjoya, x="close")

#Boxplot
#ax = sns.boxplot(x=dfjoya.index, y=dfjoya['close'], data=dfjoya)

plt.show()