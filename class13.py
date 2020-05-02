import csv
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc

import matplotlib.dates as mdates

style.use('dark_background')

Analysis='C:/Users/ccps6/Desktop/csvfile/AAPL.csv'

data=pd.read_csv(Analysis,parse_dates=True,index_col='Date')

price=data['Close']
price.head()

moveing_avg=price.rolling(20).mean()
moveing_avg50=price.rolling(50).mean()
moveing_avg80=price.rolling(80).mean()
moveing_avg_mstd=price.rolling(20).std()#標準差

top=plt.subplot2grid((12,9),(0,0),rowspan=9,colspan=9)
bottom=plt.subplot2grid((12,9),(10,0),rowspan=2,colspan=9)#兩個圖的比例大小

top.grid(which='both',alpha=0.3)

data=data.reset_index()
data['Date']=data['Date'].apply(lambda d:mdates.date2num(d.to_pydatetime()))
candlestick=[tuple(x) for x in data[['Date','Open','High','Low','Close']].values]
candlestick_ohlc(top,candlestick,width=0.5,colorup='r',colordown='green',alpha=1)



# top.plot(price,color='b')
top.plot(moveing_avg,color='r',linewidth=1,alpha=0.7,label='MA20')
top.plot(moveing_avg50,color='b',linewidth=1,alpha=0.7,label='MA50')
top.plot(moveing_avg80,color='g',linewidth=1,alpha=0.7,label='MA80')

top.fill_between(moveing_avg.index,moveing_avg-2*moveing_avg_mstd,moveing_avg+2*moveing_avg_mstd ,color='b',alpha=0.2)
bottom.bar(data.index,data['Volume'])


top.legend()
plt.show()