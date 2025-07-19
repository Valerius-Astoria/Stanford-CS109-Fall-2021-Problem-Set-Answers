import scipy.stats as stats
import math
import csv
import numpy as np
import scipy.special as special

# Points on the exam add up to 118. Calculations
# should be done based on *percent* score.
MAX_POINTS = 118

# Main: loads the true distribution
def main():
	trueDist = loadTrueDistribution()
	
# Helper method: Sterling Approximation
# approximate log(n!). Using an approximation
# is useful, but not necessary.
def sterlingApproximate(n):
	return special.gammaln(n + 1)

# Helper method: Get Problems
# Instead of loading the exam data, it
# is inlined :)
def getProblems():
	return [
		(18, 4.0),
		(24, 8.0),
		(20, 4.0),
		(22, 6.7),
		(20, 8.0),
		(14, 5.3)
	]

# Helper method: Load True Distribution
# Does what you expect. Expects a header
# line.
def loadTrueDistribution():
	fileName = 'trueDistribution.csv'
	reader = csv.reader(open(fileName))
	header = reader.next()
	dist = {}
	for row in reader:
		minRange = int(row[0])
		p = float(row[2])
		dist[minRange] = p
	return dist

if __name__ == '__main__':
	main()