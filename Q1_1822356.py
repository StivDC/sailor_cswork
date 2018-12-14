#Thomas Davies-Cortes | C1822356

import math
import random
import csv
from collections import OrderedDict

# print("#########################################################(1a)")
"""Doctest to see whether series score outputs correctly
l=("bob", [2, 4, 1, 1, 2, 5])
>>> series_score(l, 0)
15
>>> series_score(l, 1)
10
>>> series_score(l, 2)
6
"""

def series_score(x,n):
	
	#First the list (x) is sorted, then the last N elements of the list are taken away
	#After the remaining elements of the list are summed together.

	return sum(sorted(x[1])[:len(x[1])-n])
	
# print("#########################################################(1b)")

def sort_series(a, n):
	"""Doctest to see whether sort_series outputs correctly
	a=[("Alice", [1, 2, 1, 1, 1, 1]), ("Bob", [3, 1, 5, 3, 2, 5]),
	("Clare", [2, 3, 2, 2, 4, 2]), ("Dennis", [5, 4, 4, 4, 3, 4]),
	("Eva", [4, 5, 3, 5, 5, 3])]
	>>> sort_series(a, 0)
	[('Alice', [1, 2, 1, 1, 1, 1]), ('Clare', [2, 3, 2, 2, 4, 2]), ('Bob', [3, 1, 5, 3, 2, 5]), ('Dennis', [5, 4, 4, 4, 3, 4]), ('Eva', [4, 5, 3, 5, 5, 3])]
	"""
	# This uses the above function to calculate the order by which the dictionary should be ordered
	# Any ties are then sorted by the first element in the lists

	return sorted(a, key=lambda x: (series_score(x,n),x[1][0]))

	# Below, to test the function out the dictionary is printed with it's values, then without the values and just
	# as a string to make it easier to read and check.

# print("#########################################################(1c)")

from collections import OrderedDict

def read_sailor_data(filename):
	"""Doctest to see if the dictionary's are created properly from the text file
	>>> read_sailor_data("sailor_performance.csv")
	[('Dennis', (90.0, 0.0)), ('Clare', (100.0, 10.0)), ('Eva', (90.0, 5.0)), ('Bob', (100.0, 5.0)), ('Alice', (100.0, 0.0))])
	"""
	d=OrderedDict()
	with open(filename) as csvfile:
		rdr = csv.reader(csvfile)	
		for i in rdr:
			#This except is so that if the line trying to be inputted into the dictionary is a string
			#It will ignore it and go to the next line
			try: d[i[0]]=(float(i[1]),float(i[2]))
			except: None
	return d

# print("#########################################################(1d)")

def generate_perfomances(x):
	"""Doctest to check if the normal distribution values are properly outputted
	This uses the random seed of -57
	>>> random.seed(57)
	>>> generate_perfomances(read_sailor_data("sailor_perfomance.csv"))
	{'Dennis': 90.0, 'Clare': 111.52090179040226, 'Eva': 94.18226076274071, 'Bob': 101.4389222493041, 'Alice': 100.0}
	"""

	y=OrderedDict()

	# Cycles through both the values and the keys in the dictionary, creating a new dictionary which has within it
	# The names coupled with their normal distribution values

	for xValues,names in zip(x.values(),x): y[names]=random.normalvariate(xValues[0],xValues[1])
	return y

# print("#########################################################(1e)")

def calculate_finishing_order(x):
	"""Checks to see if the output value is correct (a list of strings) and the outputs are in order
	>>> calculate_finishing_order(generate_perfomances(read_sailor_data("sailor_perfomance.csv")))
	['Clare', 'Bob', 'Alice', 'Eva', 'Dennis']
	"""
	# Creates a list of keys which are sorted by their values

	return [sailor_names for sailor_names,sailorValues in sorted(x.items(), key=lambda y: y[1], reverse=True)]

# print("#########################################################(1f)")


#Generating N number of races
def simulateRaces(n):
	#generates a list called results with empty lists as values
	results={"Dennis": [], "Alice": [], "Bob": [], "Eva": [], "Clare": []}
	for i in range(1,n+1):
		GenRace = calculate_finishing_order(generate_perfomances(read_sailor_data("sailor_perfomance.csv")))
		#Appending race positions to sailors
		for sailor in enumerate(GenRace, 1):
			results[sailor[1]].append(sailor[0])
	#Sort the sailors in order of who's winning.
	positions=sort_series(list(results.items()), 1)
	# returns the names of the sorted series
	return [i[0] for i in positions]

print(simulateRaces(6))

