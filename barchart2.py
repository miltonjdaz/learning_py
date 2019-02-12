from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

url = 'http://people.terry.uga.edu/rwatson/data/manheim.txt'
data = pd.read_csv(url)

# y values - numbers
xsum = data.loc[data['model']=='X', 'price'].sum()
ysum = data.loc[data['model']=='Y', 'price'].sum()
zsum = data.loc[data['model']=='Z', 'price'].sum()
yvals = [xsum, ysum, zsum]

# x values - model names
model_list = data.model.unique()
model_list.sort()

# add it all on to the blank canvas to plot
plt.bar(model_list, yvals, align='center', alpha=0.5, color = 'red')
plt.xlabel("model")
plt.ylabel("price")
plt.title("Sum Prices for Each Model")
plt.show()
