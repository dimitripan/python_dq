# Create a python script:
#
# create list of 100 random numbers from 0 to 1000
# sort list from min to max (without using sort())
# calculate average for even and odd numbers
# print both average result in console
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.

# import random for random function
import random as r
# import numpy for average calculation
import numpy as np

# set seed so that randomizer result is always the same
r.seed(1)
# create a list with 100 random numbers from 0 to 1000
r_num_list = [r.randint(0, 1000) for x in range(100)]

# sort list with bubble sort

# set stopper
swapped = 1
# iterate through list of numbers until list is sorted
while swapped:
    # swapped = 0 means that no numbers were swapped and list is sorted
    swapped = 0
    # iterate through numbers in list
    for index in range(0, len(r_num_list) - 1):
        # compare two numbers and switch them in case the first is more than the second
        if r_num_list[index] > r_num_list[index + 1]:
            bigger = r_num_list[index]
            r_num_list[index] = r_num_list[index + 1]
            r_num_list[index + 1] = bigger
            swapped = 1

# pick odd numbers fromm previous list
odd_num = [x for x in r_num_list if x%2 == 1]

# pick even numbers from previous list
even_num = [x for x in r_num_list if x%2 == 0]

# calculate average for odd numbers
avr_odd = np.mean(odd_num)
# calculate average for even numbers
avr_even = np.mean(even_num)

# print both average result in console
print('Odd average:', round(avr_odd), 'Even average:', round(avr_even))




