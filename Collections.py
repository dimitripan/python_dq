
# Write a code, which will:
#
# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}
# Each line of code should be commented with description.
#
# Commit script to git repository and provide link as home task result.


# import random for random function
import random as r

# create list with letters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r.seed(1)
# create empty list for dictionaries
list_of_dict = []
# loop to create random number of dict from 2 to 10
for num_of_dict in range(r.randint(2, 10)):
    # create empty dict to add pairs
    create_dict = {}
    # loop to add pairs, random number of pairs from 2 to 10
    for num_of_keys in range(r.randint(2, 10)):
        # create pair where key is random letter from list and value is a random number from 0 to 100
        create_dict[letters[r.randint(0, 25)]] = r.randint(0, 100)
    # append created dict to list
    list_of_dict.append(create_dict)

# create one dict that ruled them all
common_dict = {}
# create support dict that will store information
# {letter: [dict number it came from, indicator that shows if key exist in more than one dict]}
support_dict = {}
# loop through dictionaries
for i in range(0, len(list_of_dict)):
    # loop through keys in dict
    for key in list_of_dict[i]:
        # if key already exist in common_dict
        if common_dict.get(key):
            # if stored value is less than new value
            if common_dict[key] < list_of_dict[i][key]:
                # change value to new one
                common_dict[key] = list_of_dict[i][key]
                # create/change an entry in support_dict with dict number this value came from
                # and change indicator that key exists in more than one dict
                support_dict[key] = [i+1, True]
            else:  # if stored value is bigger than new value
                # just change the indicator that that key exists in more than one dict
                support_dict[key][1] = True
        else:  # if key doesn't exist in common_dict
            # create new entry in common_dict
            common_dict[key] = list_of_dict[i][key]
            # create new entry in support_dict with dict number this value came from
            # and indicator that shows that key exist in only one dict
            support_dict[key] = [i+1, False]

# loop through keys in support keys
for key in support_dict:
    if support_dict[key][1]:  # if indicator shows that multiple keys exist
        # "rename" key
        common_dict[key + '_' + str(support_dict[key][0])] = common_dict.pop(key)
