from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd
'''style.use('ggplot')
x=[1,2,3,4,5]
y=[22,25.9,58,25,36]
x1=[1,2,3,4,5]
y2=[22,25.9,55,21,3]
plt.plot(x,y,Linewidth=3,color="red")
plt.plot(x1,y2,Linewidth=3,color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.show()'''
x=pd.period_range(pd.datetime.now(),periods=200,freq='d')
x=x.to_timestamp().to_pydatetime()

y=np.random.randn(200,3).cumsum(0)
plt.plot(x,y)
plt.show()