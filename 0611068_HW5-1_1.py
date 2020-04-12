import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#載入資料，windows的Juypter Notebook做的，所以路徑會是windows形式
read = pd.read_excel("D:/Desktop/Homework5-master/HW5-1.xls")
Y = np.array(read[['Output']])
X1 = np.array(read[['Input 1']])
X2 = np.array(read[['Input 2']])
#bias 項
X3 = np.ones(50)                 

#降維，因為是二維資料
X1 = X1.reshape(-1)
X2 = X2.reshape(-1)
Y = Y.reshape(-1)

#將X1 X2 合成一個二維矩陣
combined = np.vstack((X3,X1, X2)).T   

#theta 透過老師的公式計算出
#theta0是一個常數項 其餘是斜率
theta = np.ones(3)
theta = np.linalg.inv((combined.T).dot(combined)).dot(combined.T).dot(Y)

#使用圖形驗證
def func(x1,x2):
    return theta[0]+theta[1]*x1+theta[2]*x2
x1=np.arange(0, 50, 1)
x2=np.arange(0,160,1)

x1, x2 = np.meshgrid(x1, x2)
y = func(x1,x2)


ax = plt.subplot(projection='3d')  
ax.scatter(X1, X2, Y, c='b')
ax.plot_surface(x1, x2, y, rstride=1, cstride=1, cmap='rainbow')
ax.set_zlabel('Output') 
ax.set_ylabel('Input 2')
ax.set_xlabel('Input 1')
plt.draw()
plt.show()