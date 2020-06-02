
# coding:utf-8
 
"""
Author: roguesir
Date: 2017/8/30
GitHub: https://roguesir.github.com
Blog: http://blog.csdn.net/roguesir
"""
 
import numpy as np
import matplotlib.pyplot as plt  
x1=[1,2,3,4,5,6,7,8,9,10]
y1=[0.82,0.82,0.81,0.09,0.09,0.09,0.09,0.09,0.09,0.09]
l1=plt.plot(x1,y1,'r--',label='cat')
plt.plot(x1,y1,'ro-')

plt.xlabel('Number of eigenvectors')
plt.ylabel('Distance from original data')
plt.legend()
plt.show()