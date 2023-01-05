#import necessary packages
import numpy as np
import matplotlib as mtp
import pandas as pd
from sklearn.model_selection import train_test_split

# read the data from the dataset
dataset=pd.read("grades.csv")
data=dataset np.iloc([:,-1],[1,4])

#train the data
x=data.data
y=data.target
x_train,y_train,x_test,y_test=train_test_split(x,y,random_state=0.3,start_state=47)

from sklearn import kmeans
kmeans.fit(x_train,y_train)
c=kmeans.predict(x_test)

#plotting the values into a graph

mtp.plot.y-axis('Sr_No')
mtp.plot.x-axis('id')
mtp.show()




