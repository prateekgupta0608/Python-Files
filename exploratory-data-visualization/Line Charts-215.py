## 2. Introduction To The Data ##

import pandas as pd
unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
print(unrate.head(12))

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

rowss = unrate["DATE"].head(12)
columnz = unrate["VALUE"].head(12)
plt.plot(rowss, columnz)
plt.show()

## 8. Fixing Axis Ticks ##

rowss = unrate["DATE"].head(12)
columnz = unrate["VALUE"].head(12)
plt.plot(rowss, columnz)
plt.xticks(rotation=90)
plt.show()


## 9. Adding Axis Labels And A Title ##

rowss = unrate["DATE"].head(12)
columnz = unrate["VALUE"].head(12)
plt.plot(rowss, columnz)
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()