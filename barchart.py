from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

print('hello')
url = 'http://people.terry.uga.edu/rwatson/data/manheim.txt'
data = pd.read_csv(url)
print(data.head())

# chart = pd.max(data.price)
max = data.price.max()
print(max)
ax = df.plot(kind='bar', title ="Chart",figsize=(15,10),legend=True, fontsize=12)
ax.set_xlabel("price",fontsize=12)
ax.set_ylabel("miles",fontsize=12)