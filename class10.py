from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
style.use('ggplot')
x=[1,2,3,4,5]
y=[22,25.9,58,25,36]
x1=[1,2,3,4,5]
y2=[5,10,15,20,25]

plt.subplot(211)#2個東西要顯示 第一個東西
plt.plot(x,y,Linewidth=3,color="red",label="Apple")
plt.plot(x1,y2,Linewidth=3,color="blue",marker='o',linestyle="-",label="Google") #曲線圖
plt.legend()

plt.subplot(212)#2個東西要顯示 第二個東西
plt.bar(x,y,align='center',label="Apple")#長條圖
plt.bar(x1,y2,align='center',label="Google")
plt.legend()

plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.show()

#ctrl+/ 快速註解