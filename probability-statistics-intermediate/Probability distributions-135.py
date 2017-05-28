## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")

prob_over_5000 = (bikes[bikes["cnt"] > 5000].shape[0])/bikes.shape[0]

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
def find_probability(N, k, p, q):
    # Find the probability of any single combination.
    term_1 = p ** k
    term_2 = q ** (N-k)
    combo_prob = term_1 * term_2
    
    # Find the number of combinations.
    numerator = math.factorial(N)
    denominator = math.factorial(k) * math.factorial(N - k)
    combo_count = numerator / denominator
    
    return combo_prob * combo_count

outcome_probs = [find_probability(30, i, .39, .61) for i in outcome_counts]

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
dist = binom.pmf(outcome_counts,30,0.39)
plt.bar(outcome_counts, dist)
plt.show()

## 8. Computing the mean of a probability distribution ##

N = 30
p = 0.39
dist_mean = N*p

## 9. Computing the standard deviation ##

N = 30
p = 0.39
q = 1 - p
dist_stdev = (N*p*q)**(1/2)
print(dist_stdev)

## 10. A different plot ##

import scipy
from scipy import linspace
from scipy.stats import binom

N = 10
p = 0.39
outcome_counts = linspace(0,N,N+1)
dist = binom.pmf(outcome_counts,N,p)
plt.bar(outcome_counts, dist)
plt.show()

N = 100
p = 0.39
outcome_counts = linspace(0,N,N+1)
dist = binom.pmf(outcome_counts,N,p)
plt.bar(outcome_counts, dist)
plt.show()


## 12. Cumulative density function ##

import scipy
from scipy import linspace
from scipy.stats import binom

N = 30
p = 0.39
outcome_counts = linspace(0,N,N+1)
dist = binom.cdf(outcome_counts,N,p)
plt.plot(outcome_counts, dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

k = 16
N = 30
p = 0.39
left_16 = binom.cdf(k,N,p)
right_16 = 1 - left_16

print(left_16, right_16)