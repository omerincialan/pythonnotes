import statistics
import scipy.stats

white = []
black = []
asian = []
boys = []
girls = []

# Data from http://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014028
   
infile = open("US_ST12.TXT")
for line in infile :
   gender = line[46 : 47]
   race = line[2331 : 2332]
   minPerPeriod = int(line[248 : 252])
   periodsPerWeek = int(line[260 : 264])
   
   # codes of 0 and >= 1000 are used for invalid responses
   if minPerPeriod > 0 and minPerPeriod < 1000 and \
      periodsPerWeek > 0 and periodsPerWeek < 1000 :
      hours = minPerPeriod * periodsPerWeek / 60
      if gender == "1" :
         girls.append(hours)
      elif gender == "2" :
         boys.append(hours)
      if race == "1" :
         white.append(hours)
      elif race == "2" :
         black.append(hours)
      elif race == "3" :
         asian.append(hours)
infile.close()

print("White: %d responses, mean %f" % (len(white), statistics.mean(white)))
print("Black: %d responses, mean %f" % (len(black), statistics.mean(black)))
print("Asian: %d responses, mean %f" % (len(asian), statistics.mean(asian)))
p = scipy.stats.f_oneway(white,black,asian)[1]
print("p = %f" % p)

print("Boys: %d responses, mean %f" % (len(boys), statistics.mean(boys)))
print("Girls: %d responses, mean %f" % (len(girls), statistics.mean(girls)))
p = scipy.stats.f_oneway(boys, girls)[1]
print("p = %f" % p)

