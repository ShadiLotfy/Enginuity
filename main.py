# Please lmk with a mention that u made it to here @7ambok4a
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re


try:
    data = pd.read_csv('http://apmonitor.com/pds/uploads/Main/automotive.txt')
except Exception as e:
    print(f"Error loading data: {e}")
    exit


#set time index
data['time'] = pd.to_datetime(data['time'], format='%Y-%m-%d %H:%M:%S', errors='coerce')
data = data.set_index('time')

for x in data.columns:
    print(x)

# Remove last column with no column heading
if 'Unnamed: 22' in data.columns:
    del data['Unnamed: 22']   

#fill in NaNs - forward fill
data.ffill(inplace=True)
data.bfill(inplace=True)

# Recmove columns that match keywords "Average" or "Total" no use for those or "$"

unwanted_keywords = ["Average", "(total)", "$", "(mA)"]
escaped_keywords = [re.escape(kw) for kw in unwanted_keywords]
data = data.loc[:, ~data.columns.str.contains('|'.join(escaped_keywords), regex=True)]


print(data.head())

data.plot(subplots=True, figsize=(12,30))
plt.show()

select = ['Vehicle speed (mph)', 'Throttle position (%)', 'Engine RPM (rpm)', 'Vehicle acceleration (g)']
data[select].plot(kind = 'box', subplots=True, figsize=(12,3))
plt.show()

sns.pairplot(data[select])
plt.show()

sns.heatmap(data[select].corr())
plt.show()

