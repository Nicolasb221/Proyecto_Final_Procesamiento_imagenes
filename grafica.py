# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:01:16 2020

@author: nikob
"""

import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv('/home/nicolas/Universidad/códigos/Proyecto/datos_x', header=0, delim_whitespace=False)
data1=pd.read_csv('/home/nicolas/Universidad/códigos/Proyecto/datos_y', header=0, delim_whitespace=False)


x=data.loc[:,'# x']
y=data1.loc[:,'# y']

print(x)
print(y)

plt.plot(x,y,'ro')
plt.ylabel('y')
plt.xlabel('x')
plt.show