import numpy as np
import pandas as pd
# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

dict_ex = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
     'Italy': [6, 8, 1, 7]}
# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def total_registered_cases(data, country):
    return np.sum(np.array(data[country]))

print(total_registered_cases(dict_ex, "Spain"))
# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
#

def total_registered_cases_per_country(data):
    summerized_dict = dict()

    countries_list = data.keys()
    
    for country in countries_list:
        total_cases = total_registered_cases(data, country)
        summerized_dict[country] = total_cases

    return summerized_dict
print(total_registered_cases_per_country(dict_ex))
# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data):

    values_list = list(total_registered_cases_per_country(data).values())
    keys_list = list(total_registered_cases_per_country(data).keys())

    max_val = np.max(values_list)
    pos_max_val = values_list.index(max_val)

    return keys_list[pos_max_val]

print(country_with_most_cases(dict_ex))