#importing plotly and pandas
import plotly.express as px
import pandas as pd 

# read the files 
rd = pd.read_csv('iceCream.csv')

#plotting the graph
gr = px.scatter(rd, x ='Temperature',y = 'Ice-cream Sales')
gr.show()

# read the files 
rd1 = pd.read_csv('coffee.csv')

#plotting the graph
gr1 = px.scatter(rd1, x ='Coffee in ml',y = 'sleep in hours')
gr1.show()

#read the file
df = pd.read_csv('marks.csv')


#importing numpy 
import numpy as np 

#making the matrix of the corelation
cof = np.corrcoef(df['Marks In Percentage'],df['Days Present'])
print(cof)





