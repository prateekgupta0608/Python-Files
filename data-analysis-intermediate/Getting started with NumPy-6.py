## 2. Lists of lists ##

import csv

with open('world_alcohol.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    world_alcohol = list(reader)
years = []
for row in world_alcohol:
    years_y = row[0]
    years.append(years_y)
years = years[1:len(years)]
    
total = 0
for item in years:
    total = total + float(item)
avg_year = total / len(years)
print(avg_year)

## 4. Using NumPy ##

import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
print(type(world_alcohol))

## 5. Creating arrays ##

import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

## 6. Array shape ##

vector = numpy.array([10, 20, 30])
vector_shape = vector.shape
matrix = numpy.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
matrix_shape = matrix.shape
print(vector_shape)
print(matrix_shape)

## 7. Data types ##

import numpy
world_alcohol = numpy.genfromtxt("world_alcohol.csv", delimiter=",")
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)

## 9. Reading in the data properly ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', dtype='U75', delimiter=',', skip_header=1)
print(world_alcohol)

## 10. Indexing arrays ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', dtype='U75', delimiter=',', skip_header=1)
uruguay_other_1986 = world_alcohol[1,4]
third_country = world_alcohol[2,2]
print(uruguay_other_1986, third_country)

## 11. Slicing arrays ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', dtype='U75', delimiter=',', skip_header=1)
countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]
print(countries)
print(alcohol_consumption)

## 12. Slicing one dimension ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', dtype='U75', delimiter=',', skip_header=1)
first_two_columns = world_alcohol[:,0:2]
first_ten_years = world_alcohol[0:10,0]
first_ten_rows = world_alcohol[0:10, :]

## 13. Slicing arrays ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', dtype='U75', delimiter=',', skip_header=1)
first_twenty_regions = world_alcohol[0:20,1:3]