## 
# This program prints information about the current weather in a user-chosen 
# city.
#

import urllib.request
import urllib.parse
import json

# Get the location information from the user.
city = input("Enter the location: ")

# Build and encode the URL parameters.
params = {"q": city, "units": "imperial" }
arguments = urllib.parse.urlencode(params)

# Get the weather information.
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

webData = urllib.request.urlopen(url)
results = webData.read().decode()
webData.close()

# Convert the json result to a dictionary.
data = json.loads(results)

# Print the results.
current = data["main"]
degreeSym = chr(176)
print("Temperature: %d%sF" % (current["temp"], degreeSym))
print("Humidity: %d%%" % current["humidity"])
print("Pressure: %d" % current["pressure"])

