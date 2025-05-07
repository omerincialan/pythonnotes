import csv
import scipy.stats
import matplotlib.pyplot

lifeexp = []
healthex = []

reader = csv.reader(open("oecd.csv"))
next(reader) # Skip header row
for row in reader :
   lifeexp.append(float(row[2]))
   healthex.append(float(row[4]))

r = scipy.stats.linregress(healthex, lifeexp)
slope = r[0]
intercept = r[1]
correlation = r[2]
print("Correlation coefficient: %f" % correlation)

matplotlib.pyplot.scatter(healthex, lifeexp)

x1 = min(healthex)
y1 = intercept + slope * x1
x2 = max(healthex)
y2 = intercept + slope * x2
matplotlib.pyplot.plot([x1,x2],[y1,y2])
matplotlib.pyplot.show()
