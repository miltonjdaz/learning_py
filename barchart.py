import pandas as pd 

print('hello')
url = 'http://people.terry.uga.edu/rwatson/data/manheim.txt'
data = pd.read_csv(url)
print(data.head())
