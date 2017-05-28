## 2. Array Comparisons ##

countries = world_alcohol[:,2]
countries_canada = countries == 'Canada'
years = world_alcohol[:,0]
years_1984 = years == '1984'

## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986, :]

## 5. Replacing Values ##

is_1986 = world_alcohol[:,0] == '1986'
world_alcohol[is_1986, 0] = '2014'
is_wine = world_alcohol[:,3] == 'Wine'
world_alcohol[is_wine,3] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty, 4] = '0'

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)
print(alcohol_consumption)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_1986_canada = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Canada')
canada_1986 = world_alcohol[is_1986_canada, :]
is_value_empty = canada_1986[:,4] == ''
canada_1986[is_value_empty, 4] = '0'
canada_alcohol = canada_1986[:,4]
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
is_1989 = world_alcohol[:,0] == '1989'
year = world_alcohol[is_1989, :]

for country in countries:
   is_country = year[:,2] == country
   country_consumption = year[is_country,:]
   is_value_empty = country_consumption[:,4] == ''
   country_consumption[is_value_empty, 4] = '0'
   country_alcohol = country_consumption[:,4]
   country_alcohol = country_alcohol.astype(float)
   totals[country] = country_alcohol.sum()

   
print(totals)

   

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
countries = totals.keys()
for country in countries:
    if totals[country] > highest_value:
        highest_value = totals[country]
        highest_key = country
      
   
print(highest_value, highest_key)
        