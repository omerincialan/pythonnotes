##
#  This program reads data files of country populations and areas and prints the
#  population density for each country.
#

POPULATION_FILE = "worldpop.txt"
AREA_FILE = "worldarea.txt"
REPORT_FILE = "world_pop_density.txt"

def main() :
   # Open the files.
   popFile = open(POPULATION_FILE, "r")
   areaFile = open(AREA_FILE, "r")
   reportFile = open(REPORT_FILE, "w")

   # Read the first population data record.
   popData = extractDataRecord(popFile)
   while len(popData) == 2 :
      # Read the next area data record.
      areaData = extractDataRecord(areaFile)
      
      # Extract the data components from the two lists.
      country = popData[0]
      population = popData[1]
      area = areaData[1]
      
      # Compute and print the population density.
      density = 0.0
      if area > 0 :   # Protect against division by zero.
         density = population / area
      reportFile.write("%-40s%15.2f\n" % (country, density))
      
      # Read the next population data record.
      popData = extractDataRecord(popFile)
      
   # Close the files.
   popFile.close()
   areaFile.close()
   reportFile.close()
   
## Extracts and returns a record from an input file in which the data is
#  organized by line. Each line contains the name of a country (possibly 
#  containing multiple words) followed by an integer (either population
#  or area for the given country). 
#  @param infile the input text file containing the line oriented data
#  @return a list containing the country (string) in the first element
#  and the population (int) or area (int) in the second element. If the end of
#  file was reached, an empty list is returned.
#
def extractDataRecord(infile) :
   line = infile.readline()
   if line == "" :
      return []
   else :
      parts = line.rsplit(" ", 1)
      parts[1] = int(parts[1]) 
      return parts
      
# Start the program.
main()

