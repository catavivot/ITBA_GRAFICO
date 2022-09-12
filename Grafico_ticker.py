import sqlite3
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

conn = sqlite3.connect('tickers.db') 
          
sql_query = pd.read_sql_query ('''
                               SELECT
                               Ticker, Date, Open, Close, High, Low
                               FROM tickers
                               ORDER BY Date ASC;
                               ''', conn)

#Armamos un Data Frame de la base de datos para graficar
prices = pd.DataFrame(sql_query, columns = ['Ticker', 'Date', 'Open', 'Close', 'High', 'Low'])
print (prices)

#Saco las horas de la fecha para el gráfico
prices['Date'] = pd.to_datetime(prices['Date']).dt.date
print (prices['Date'])
#La hago index para que me lo tome como el eje x. 
prices.set_index('Date', inplace=True)

fig, ax = plt.subplots(2, 1)
plt.rcParams["figure.figsize"] = [10, 10]
plt.rcParams["figure.autolayout"] = True

#Graficamos uno de líneas
plt.subplot(212)
ax = plt.gca()

prices.plot(kind='line',y='Open', color='orange', ax=ax)
prices.plot(kind='line',y='Close', color='blue', ax=ax)
prices.plot(kind='line',y='High', linestyle='--', color='greenyellow', ax=ax)
prices.plot(kind='line',y='Low', linestyle='--', color='r', ax=ax)

#Roto el x-axis tick labels
plt.xticks(rotation=45, ha='right')

#Agrego los títulos de los ejes y la leyenda
plt.legend(1.1, 0.1)

#Graficamos un boxplot 
##ax = plt.figure()
plt.subplot(211)

#Defino el ancho de los boxplots
width = 2
width2 = .5

#Defino los precios up y down
up = prices[prices.Close>=prices.Open]
down = prices[prices.Close<prices.Open]

#Defino los colores 
col1 = 'green'
col2 = 'red'

#Grafico los up prices
plt.bar(up.index, up.Close-up.Open, width, bottom=up.Open, color=col1)
plt.bar(up.index, up.High-up.Close, width2, bottom=up.Close, color=col1)
plt.bar(up.index, up.Low-up.Open, width2, bottom=up.Open, color=col1)

#Grafico los down prices
plt.bar(down.index, down.Close-down.Open, width, bottom=down.Open, color=col2)
plt.bar(down.index, down.High-down.Open, width2, bottom=down.Open, color=col2)
plt.bar(down.index, down.Low-down.Close, width2, bottom=down.Close, color=col2)

#Roto el x-axis tick labels
plt.xticks(rotation=45, ha='right')

#Agrego los títulos de los ejes
plt.xlabel('Date')


#Imprimo
plt.show()
