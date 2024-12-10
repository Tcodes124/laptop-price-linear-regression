import pandas as pd
import matplotlib.pyplot as plt
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


def plot_predicted_line(m):
    xpoints_pred=[]
    x=0
    while x<5:
        xpoints_pred.append(x)
        x+=0.1
    ypoints_pred=[]
    for i in xpoints_pred:
        ypoints_pred.append(i*m)

    xpoints_pred=np.array(xpoints_pred)
    ypoints_pred=np.array(ypoints_pred)
    plt.plot(xpoints_pred,ypoints_pred)



#Find where error value is lowest based on slope value
def cost_function(range_of_slopes):
    m=-1*range_of_slopes
    xpoints_error=[] #is equal to slope value
    ypoints_error=[] #is equal to error value
    while m<range_of_slopes:
        total=0
        for i in range(len(price)):
            total+=((m*weight[i]-price[i]))**2
        error=total/(2*len(price))
        ypoints_error.append(error)
        xpoints_error.append(m)
        m+=1
    
    x=np.array(xpoints_error)
    y=np.array(ypoints_error)
    plt.subplot(1,2,2)
    plt.plot(x,y)
    plt.title('Cost Function Error')
    plt.ylabel('J(m)')
    plt.xlabel('m')

    sorted_arr=np.sort(y)
    loc_lowest=np.where(y==sorted_arr[0])
    slope=x[loc_lowest]
    print(slope)
    return slope

slope=(cost_function(3000))



#Plot Data Points
xpoints_points=weight
ypoints_points=price
plt.subplot(1,2,1)
plt.plot(xpoints_points,ypoints_points,'o',ms=1)
plot_predicted_line(slope)
plt.title('Data Points')
plt.ylabel('Price (euro)')
plt.xlabel('Weight (kg)')

#Plot Everything
plt.suptitle("Laptop Weight to Price Linear Regression Model")
plt.show()