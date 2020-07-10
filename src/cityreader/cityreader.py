# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []
class City:
  def __init__(self, city, state_name, county_name, lat, lng, population, density, timezone, zips):
    self.city = city
    self.state_name = state_name
    self.county_name = county_name
    self.lat = float(lat)
    self.lng = float(lng)
    self.population = population
    self.density = density
    self.timezone = timezone
    self.zips = zips
  def __str__(self):
    return {"city":self.city, 
            "state_name": self.state_name, 
            "county_name": self.county_name, 
            "lat": self.lat, 
            "lng": self.lng, 
            "population": self.population, 
            "density": self.density, 
            "timezone": self.timezone,
            "zips": self.zips
            }

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    f = open('src/cityreader/cities.csv', 'r')
    next(f)
    for line in f:
      arglist = []
      arglist = line.split(",")
      newCity = City(*arglist)
      cities.append(newCity)
    return cities

cityreader(cities)
# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(f"{c.city}: {c.lat}, {c.lng}")

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  upperLat = None
  lowerLat = None
  upperLon = None
  lowerLat = None

  if lat1 > lat2:
    upperLat = lat1
    lowerLat = lat2
  elif lat2 >= lat1:
    upperLat = lat2
    lowerLat = lat1
  
  if lon1 > lon2:
    upperLon = lon1
    lowerLon = lon2
  elif lon2 >= lon1:
    upperLon = lon2
    lowerLon = lon1

  within = [c for c in cities if upperLat >= c.lat >= lowerLat and upperLon >= c.lng >= lowerLon]

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within
while True:
  try:
    latA, lonA = input("Enter the first set of coordinates (x,y): ").split(",")
    latB, lonB = input("Enter the second set of coordinates (x,y): ").split(",")

    latA = float(latA)
    lonA = float(lonA)
    latB = float(latB)
    lonB = float(lonB)

    result = []

    result = cityreader_stretch(latA, lonA, latB, lonB, cities)
  except: print("please enter valid coordinates")
  else:
    for c in result:
      print(f"{c.city}: {c.lat}, {c.lng}")