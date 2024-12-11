import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np


#Obtain only weight and price data for training set
file=pd.read_csv("laptop-dataset.csv")
df=pd.DataFrame(file)

#To dollar conversion
price=[]
for i in df['Price (Euro)']:
    price.append(i+1.05)

#Turn into lists for plotting
price=np.array(price)
weight=np.array(df['Weight (kg)'])

#New Dataframe with just the two info columns
two_info_df=pd.DataFrame({"Price":price,"Weight":weight})

#Error Function
def error_calculate(slope,b):
    total=0
    for i in range(len(price)):
        total+=(((slope*weight[i]+b)-price[i]))**2
    error=total/(2*len(price))
    return error


#plot 3D mesh of error rates
ax=plt.axes(projection='3d')

m_data=np.arange(-3000,3000,1)
b_data=np.arange(0,5000,1)

X,Y = np.meshgrid(m_data,b_data)
Z=error_calculate(X,Y)

ax.plot_surface(X,Y,Z, cmap="viridis")
plt.show()

#Calculate line of best fit
# def line_best():
#     error_data=[]
#     m_data=range(-3000,3000,1)
#     b_data=range(0,5000,1)
#     for i in m_data:
#         for b in b_data:
#             error_data.sort()
#             if error_data[0]==:
#                 return i,b
#             error_data.append(error_calculate(i,b))
#     #stop when error data reahces a minimum
    
#     print(error_data[0])
# best_slope,best_intercept=line_best()

#plot line of best fit
def plot_predicted_line(m,b):
    xpoints_pred=[]
    x=0
    while x<5:
        xpoints_pred.append(x)
        x+=0.1
    ypoints_pred=[]
    for i in xpoints_pred:
        ypoints_pred.append(i*m+b)

    xpoints_pred=np.array(xpoints_pred)
    ypoints_pred=np.array(ypoints_pred)
    plt.plot(xpoints_pred,ypoints_pred)

#Plot Data Points
xpoints_points=weight
ypoints_points=price
plt.plot(xpoints_points,ypoints_points,'o',ms=1)
# plot_predicted_line(best_slope,best_intercept)
plt.ylabel('Price (euro)')
plt.xlabel('Weight (kg)')

#Plot Everything
plt.suptitle("Laptop Weight to Price Linear Regression Model")
plt.show()