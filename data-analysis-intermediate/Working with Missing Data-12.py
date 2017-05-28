## 1. Introduction ##

import pandas as pd

titanic_survival = pd.read_csv("titanic_survival.csv")

## 2. Finding the Missing Data ##

age = titanic_survival["age"]
age_is_null = pd.isnull(age)
age_null_true = age[age_is_null]
age_null_count = len(age_null_true)
print(age_null_count)

## 3. Whats the big deal with missing data? ##

age_is_null = pd.isnull(titanic_survival["age"])
good_ages = titanic_survival["age"][age_is_null == False]
correct_mean_age = sum(good_ages) / len(good_ages)

## 4. Easier Ways to Do Math ##

correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare = titanic_survival["fare"].mean()

## 5. Calculating Summary Statistics ##

passenger_classes = [1, 2, 3]
fares_by_class = {}

for this_class in passenger_classes:
    pclass_rows = titanic_survival[titanic_survival["pclass"] == this_class]
    pclass_fares = pclass_rows["fare"]
    fare_for_class = pclass_fares.mean()
    fares_by_class[this_class] = fare_for_class
    
print(fares_by_class)

## 6. Making Pivot Tables ##

passenger_age = titanic_survival.pivot_table(index="pclass", values="age")
print(passenger_age)

## 7. More Complex Pivot Tables ##

import numpy as np
port_stats = titanic_survival.pivot_table(index="embarked", values= ["fare", "survived"], aggfunc=np.sum)
print(port_stats)


## 8. Drop Missing Values ##

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis=1)
new_titanic_survival = titanic_survival.dropna(axis=0,subset=["age", "sex"])

## 9. Using iloc to Access Rows by Position ##

# We have already sorted new_titanic_survival by age
first_five_rows = new_titanic_survival.iloc[0:5]
first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]

## 10. Using Column Indexes ##

five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]
row_index_1100_age = new_titanic_survival.loc[1100,"age"]
row_index_25_survived = new_titanic_survival.loc[25,"survived"]

## 11. Reindexing Rows ##

titanic_reindexed = new_titanic_survival.reset_index(drop=True)
five_rows_three_cols = titanic_reindexed.iloc[0:5,0:3]
print(five_rows_three_cols)


## 12. Apply Functions Over a DataFrame ##

def not_null_count(column):
    column_null = pd.isnull(column)
    null = column[column_null]
    return len(null)

column_null_count = titanic_survival.apply(not_null_count)

## 13. Applying a Function to a Row ##

def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)
import pandas as pd

def generate_age_label(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age < 18:
        return "minor"
    else:
        return "adult"

age_labels = titanic_survival.apply(generate_age_label, axis=1)

## 14. Calculating Survival Percentage by Age Group ##

age_group_survival = titanic_survival.pivot_table(index="age_labels", values="survived")