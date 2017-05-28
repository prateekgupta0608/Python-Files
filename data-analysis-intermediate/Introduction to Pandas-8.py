## 3. Read in a CSV file ##

import pandas
food_info = pandas.read_csv("food_info.csv")

print(type(food_info))

## 4. Exploring the DataFrame ##

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)

first_twenty = food_info.head(20)

## 7. Selecting a row ##

hundredth_row = food_info.loc[99]

print(hundredth_row)

## 9. Selecting multiple rows ##

dimensions = food_info.shape
num_rows = dimensions[0]
last_rows = food_info.loc[(num_rows - 5):num_rows]
print(last_rows)

## 10. Selecting individual columns ##

saturated_fat = food_info["FA_Sat_(g)"]
cholesterol = food_info["Cholestrl_(mg)"]

## 11. Selecting multiple columns by name ##

selenium_thiamin = food_info[["Selenium_(mcg)", "Thiamin_(mg)"]]
print(selenium_thiamin)

## 12. Practice ##

column_names = food_info.columns
columns_list = column_names.tolist()
gram_columns = []

for col_name in columns_list:
    if col_name.endswith("(g)"):
        gram_columns.append(col_name)
        
gram_df = food_info[gram_columns]
print(gram_df.head(2))