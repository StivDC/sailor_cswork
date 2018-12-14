#Thomas Davies-Cortes | C1822356
from Q1_1822356 import simulateRaces
import functools
import matplotlib.pyplot as plt

def Average(lst): 
	# adds each value in a list and divides it by the length of the list giving it its average
	return functools.reduce(lambda a, b: a+b, lst) / len(lst)

def plotPosAvg(a):
	# For the length of the list of values
	for i in range(len(a)):
		newList=[]
		newAvgList=[]
		# For each value in the list
		for x in a:
			# adds a series position to a new list
			newList.append(x)
			# creates a temporary average value which is an average of the new list 
			tempAvg = Average(newList)
			# Appends the average of the newList into a list which will be plotted on the graph
			newAvgList.append(int(tempAvg))
	return(newAvgList)

def plotCharts(x, n):
	# Generator expression to make a list for every value from 1 to N
	xAxis = [i for i in range(1,n+1)]
	avgPosition = []
	for pos in x.values():
		# Plots the average values onto a graph for each sailor
		plt.plot(xAxis, plotPosAvg(pos), linewidth=2.5)
		# Gathers an overall average for each Sailor to be used later
		avgPosition.append(Average(pos))
	# Makes the legend (the key) equal the all the names in the dictionary
	legend=[i for i in x.keys()]
	plt.legend(legend)
	plt.xlabel("Race number")
	plt.ylabel("Positions")
	plt.title("Fairness of sailing scoring")
	# prints the names
	print(legend)
	# prints the averages for each sailor
	print(avgPosition)
	plt.show()

def gatherData(x):
	axisDict = {}
	# Used to get the names of the dictionary
	oldDict = simulateRaces(2)
	#Creates a new dictionary with the names of sailors as keys and an empty list as values 
	for i in range(len(oldDict)): axisDict[oldDict[i]]=[]
	# for c in oldDict: axisDict[c[0]]=[]
	for i in range(x):
		# simulates 6 races
		racePos = simulateRaces(6)
		# gets the overall positions of the simulate races
		for z in enumerate(racePos, 1):
			# appends the overall positions to the names in the new dictionary
			axisDict[z[1]].append(z[0])
	plotCharts(axisDict, x)
gatherData(100)
