import csv
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style


Analysis='C:/Users/ccps6/Desktop/csvfile/Data.txt'

csv_file='C:/Users/ccps6/Desktop/csvfile/Data.csv'

# open_txt=csv.reader(open(Analysis, 'r'),delimiter=',')
#
# out_csv=csv.writer(open(csv_file,'w',newline=''))
#
# out_csv.writerow(['筆數','價格'])
# out_csv.writerows(open_txt)

data=pd.read_csv(csv_file, parse_dates=True, index_col='筆數')#parse_date:資料整理

plt.plot(data['價格'])
plt.show()